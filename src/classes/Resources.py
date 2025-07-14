## Import all the libraries
import pyglet as pg, gc, struct
from SpecialIsResourceDataLoadable import is_it

## Resources
class Resource:
    def __init__(self, data="", type="str", path="test.png", parameters={}):
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
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())

    def discard(self):
        # Remove resource
        del self.data
        del self.path
        del self
        gc.collect()

class Image(Resource):
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
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"IMS")
            try:
                cx, cy, cw, ch = self.para["clip"]
            except:
                cx, cy, cw, ch = 0
            f.write(struct.pack("<II", self.width, self.height))
            f.write(struct.pack("<IIII", cx, cy, cw, ch))
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())

class Media(Resource):
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"MED")

def img_to_sheet(img, clip = 0):
    paran = img.para.copy()
    paran["clip"] = clip
    
    ims = SheetImage(img.get(), img.type, img.path, paran)

    return ims

class Script(Resource):
    def on_ready(self):
        self.contents = self.data
        self.language = self.contents.splitlines()[0]
    
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"SCR")
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())
    
## Loader class
class Loader:
    def __init__(self, Data):
        self.game_data     = Data
        self.resource_tree = {}
    
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
                        assetres = Image(asset, "sprite", actual_path)
                    elif actual_path.split(".")[-1].lower() in ("mp3","ogg","wav","mp4","webm","avi","mpeg"):
                        asset = pg.resource.media(actual_path)
                        assetres = Media(asset, "med", actual_path)
                    else:
                        asset = pg.resource.file(actual_path, "r").read()
                        assetres = Script(asset, "str", actual_path)
                else:
                    if path.startswith("user:"):
                        actual_path = self.game_data.data_directory + path.lstrip("user:")
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
                    else:
                        asset = open(actual_path).read()
                        assetres = Script(asset, "str", actual_path)
                assetres.serialize(actual_path+".tres")
                
                self.resource_tree[location] = assetres
                return assetres