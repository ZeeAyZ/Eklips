## Import all the libraries
import pyglet as pg, gc, struct
from SpecialIsResourceDataLoadable import is_it

## Resources
class Resource:
    """The main Resource object. This stores nothing, but all other Resources uses this class as a base."""
    def __init__(self, data="", type="str", path="nothing.txt", parameters={}):
        """Initalize the Resource object."""
        self.data = data
        self.para = parameters
        self.type = type
        self.path = path
        self.on_ready()
        print(f"    ~ Loading resource of type {type}")
    
    def get(self):
        # Get the resource data (`Sprite`, `Image`, `Script`, etc..)
        return self.data
    
    def get_path(self):
        # Get the resource path (`res:/test.png`, etc..)
        return self.path
    
    def on_ready(self):
        pass

    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"RSC")
            f.write(struct.pack("<I", len(self.get())))
            f.write(self.get().encode())

    def discard(self):
        # Remove resource
        del self.data
        del self.path
        del self
        gc.collect()

class Image(Resource):
    """This resource stores a Sprite. you may get only the image by getting the `image` variable. Calling `get()` gives the sprite."""
    def on_ready(self):
        self.image  = self.data.image
        self.sprite = self.data
        self.width  = self.image.width
        self.height = self.image.height
    
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"IMG")
            f.write(struct.pack("<II", self.width, self.height))
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())

class SheetImage(Image):
    """A portion of a spritesheet image. Works just like a regular image resource, but saved differently."""
    def on_ready(self):
        self.image  = self.data.image
        self.sprite = self.data
        self.width  = self.image.width
        self.height = self.image.height
        self._clip()
    
    def _clip(self):
        if self.para["clip"]:
            ## Clipping
            cx, cy, cw, ch = self.para["clip"]
            cy = self.image.height - cy - ch

            self.image = self.image.get_region(cx, cy, cw, ch)
    
    def serialize(self, path):
        """Save the resource into a file"""
        with open(path, "wb") as f:
            f.write(b"IMS")
            try:
                cx, cy, cw, ch = self.para["clip"]
            except:
                cx, cy, cw, ch = 0, 0, 0, 0
            f.write(struct.pack("<II", self.width, self.height))
            f.write(struct.pack("<IIII", cx, cy, cw, ch))
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())

class Media(Resource):
    """Mediafile resource. Can be video or audio."""
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"MED")

class Script(Resource):
    """A Script file."""
    def on_ready(self):
        self.contents = self.data
        self.language = self.contents.splitlines()[0]
    
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"SCR")
            f.write(struct.pack("<I", len(self.get())))
            f.write(self.get().encode())
    
## Functions
def img_to_sheet(img, clip = 0):
    """Convert a spritesheet image to only a part of it."""
    paran = img.para.copy()
    paran["clip"] = clip
    
    ims = SheetImage(img.get(), img.type, img.path, paran)

    return ims

## Loader class
class Loader:
    def __init__(self, Data, save):
        self.game_data     = Data
        self.save          = save
        self.resource_tree = {}
    
    def load_from_resf(self,data):
        """
        This function takes a file stream of a .RES file and returns a Resource object with the data in that .RES file.
        """
        obj = 0

        with data as f:
            type = f.read(3)
            print(type)

            if type == b"MED": return Media()
            if type == b"SCR":
                dal = f.read(struct.unpack("<I", f.read(4))) # Data length
                dat = f.read(dal).decode()
                obj = Script(dat)
            if type == b"SCR":
                dal = f.read(struct.unpack("<I", f.read(4))) # Data length
                dat = f.read(dal).decode()
                obj = Script(dat)
            if type == b"RES":
                dal = f.read(struct.unpack("<I", f.read(4))) # Data length
                dat = f.read(dal).decode()
                obj = Resource(dat)
            if type == b"IMG":
                w,h = f.read(struct.unpack("<II", f.read(8))) 
                dal = f.read(struct.unpack("<I", f.read(4)))  # Data length
                dat = f.read(dal).decode()
                obj = Image(self.load(dat), path=dat)
            if type == b"IMS":
                w,h            = f.read(struct.unpack("<II", f.read(8)))    
                cx, cy, cw, ch = f.read(struct.unpack("<IIII", f.read(16))) 

                clip           = [cx,cy,cw,ch]
                if clip == [0,0,0,0]:
                    clip       = 0
                
                dal            = f.read(struct.unpack("<I", f.read(4)))     # Data length
                dat            = f.read(dal).decode()
                obj            = SheetImage(self.load(dat), path=dat, parameters={"clip":clip})
        
        return obj
    
    def load(self, path, can_cache=1):
        ## Load a resource. Specify path "`user:/..`", "`res:/..`" or "`program:/..`"
        asset       = 0
        type        = "mm"
        location    = path.lstrip("res:").lstrip("program:/")
        actual_path = location
        if can_cache:
            if location in self.resource_tree:
                asset = self.resource_tree[location]
                return asset
            else:
                print(f"  ~ Loading file {path}")
                if path.startswith("program:") and not is_it:
                    path = path.lstrip("program:/")
                if path.startswith("program:"):
                    actual_path = path.lstrip("program:/")
                    if actual_path.split(".")[-1].lower() in ("png","jpg","jpeg","webp"):
                        asset = pg.sprite.Sprite(pg.resource.image(actual_path))
                        assetres = Image(asset, "sprite", path)
                    elif actual_path.split(".")[-1].lower() in ("mp3","ogg","wav","mp4","webm","avi","mpeg"):
                        asset = pg.resource.media(actual_path)
                        assetres = Media(asset, "med", path)
                    elif actual_path.split(".")[-1].lower() in ("res"):
                        asset = pg.resource.file(actual_path, "rb")
                        assetres = self.load_from_resf(asset)
                    else:
                        asset = pg.resource.file(actual_path, "r").read()
                        assetres = Script(asset, "str", path)
                else:
                    if path.startswith("user:"):
                        actual_path = self.save + path.lstrip("user:")
                    elif path.startswith("res:"):
                        actual_path = self.game_data.data_directory + path.lstrip("res:")
                    else:
                        actual_path = path
                    if actual_path.split(".")[-1].lower() in ("png","jpg","jpeg","webp","bmp","dds"):
                        asset = pg.sprite.Sprite(pg.image.load(actual_path))
                        assetres = Image(asset, "sprite", actual_path)
                    elif actual_path.split(".")[-1].lower() in ("mp3","ogg","wav","mp4","webm","avi","mpeg"):
                        asset = pg.media.load(actual_path)
                        assetres = Media(asset, "med", actual_path)
                    elif actual_path.split(".")[-1].lower() in ("res", "import"):
                        asset = open(actual_path,"rb")
                        assetres = self.load_from_resf(asset)
                    else:
                        asset = open(actual_path).read()
                        assetres = Script(asset, "str", actual_path)
                
                assetres.serialize(actual_path+".import")
                
                self.resource_tree[location] = assetres
                return assetres