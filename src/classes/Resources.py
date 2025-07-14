## Import all the libraries
import pyglet as pg, json
from SpecialIsResourceDataLoadable import is_it

class Resource:
    def __init__(self, data="", type="str", path="test.png", parameters={}):
        self.data = data
        self.para = parameters
        self.type = type
        self.path = path
        self.on_ready()
        print(f"    ~ Loading resource of type {type}")
    
    def get(self):
        return self.data
    
    def get_path(self):
        return self.path
    
    def on_ready(self):
        pass

    def discard(self):
        del self.data
        del self.path
        del self

class Image(Resource):
    def on_ready(self):
        self.image  = self.data.image
        self.sprite = self.data
        self.width  = self.image.width
        self.height = self.image.height

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

class Media(Resource):
    pass

def img_to_sheet(img, clip = 0):
    paran = img.para.copy()
    paran["clip"] = clip
    
    ims = SheetImage(img.get(), img.type, img.path, paran)

    return ims

class Script(Resource):
    def on_ready(self):
        self.contents = self.data
        self.language = self.contents.splitlines()[0]
    
    def serialize(self):
        dat = {
            "con": self.contents,
            "lan":     "Eklips 4.0A"
        }
        return dat
    
## Loader class
class Loader:
    def __init__(self, Data):
        self.game_data     = Data
        self.resource_tree = {}
    
    def load(self, path, can_cache=1):
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
                
                self.resource_tree[location] = assetres
                return assetres