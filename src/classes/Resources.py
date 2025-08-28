## Import all the libraries
import pyglet as pg, gc, struct, types, sys, io
import pygame as pyg
from pygame.mixer import Sound
from anytree import NodeMixin
from classes.Object import Object
from SpecialIsResourceDataLoadable import IS_IT as IS_EXECUTABLE
import classes.Singleton as engine

## Mixer
pyg.mixer.init()

## Resources
global_res_len = 0
class Resource(Object):
    """The main Resource object. This stores nothing, but all other Resources uses this class as a base."""

    res_base_data = {
        "prop":   {},
        "data":   {
            "object": None,
            "path":   "res://"
        },
        "meta":   {
            "kind": "Resource",
            "name": "Resource"
        },
        "script": None
    }
    def __init__(self, data=res_base_data):
        super().__init__(data)
    
    def get(self):
        # Get the resource data (`Sprite`, `Image`, `Script`, etc..)
        return self.data["object"]
    
    def get_path(self):
        # Get the resource path (`res://test.png`, etc..)
        return self.data["path"]

    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"RSC")
            f.write(struct.pack("<I", len(self.get())))
            f.write(self.get().encode())

class Image(Resource):
    """This resource stores an Image. you may get only the image by getting the `image` variable."""

    img_base_data = {
        "prop":   {},
        "data":   {
            "object": None,
            "path":   "res://"
        },
        "meta":   {
            "kind": "Resource",
            "name": "Image"
        },
        "script": None
    }
    def __init__(self, data=img_base_data):
        super().__init__(data)
        self.image  = self.data["object"]
        self.width  = self.image.width
        self.height = self.image.height
    
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"IMG")
            f.write(struct.pack("<II", self.width, self.height))
            f.write(struct.pack("<I", len(self.get_path())))
            f.write(self.get_path().encode())

class SheetImage(Resource):
    """A portion of a spritesheet image. Works just like a regular image resource, but saved differently."""

    img_base_data = {
        "prop":   {},
        "data":   {
            "object": None,
            "path":   "res://",
            "clip":   [0,0]
        },
        "meta":   {
            "kind": "Resource",
            "name": "SheetImage"
        },
        "script": None
    }
    def __init__(self, data=img_base_data):
        super().__init__(data)
        self.image  = self.data["object"]
        self.width  = self.image.width
        self.height = self.image.height
        self.sheet  = self.image
        self._clip()
    
    def _clip(self):
        if self.data["clip"]:
            ## Clipping
            cx, cy, cw, ch = self.data["clip"]
            cy             = (self.height - ch) - cy

            self.image          = self.image.get_region(cx, cy, cw, ch)
            self.data["object"] = self.image
            self.height         = ch
            self.width          = cw
    
    def serialize(self, path):
        """Save the resource into a file"""
        with open(path, "wb") as f:
            f.write(b"IMS")
            try:
                cx, cy, cw, ch = self.para["clip"]
            except:
                cx, cy, cw, ch = 0, 0, self.sheet.width, self.sheet.height
            f.write(struct.pack("<II", cw, ch))
            f.write(struct.pack("<II", cx, cy))
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

    scr_base_data = {
        "prop":   {},
        "data":   {
            "object": "# python 3.13\n",
            "path":   "res://"
        },
        "meta":   {
            "kind": "Resource",
            "name": "Script/Python/EklipsContext"
        },
        "script": None
    }
    def __init__(self, data=scr_base_data):
        super().__init__(data)
        self.scriptpath = self.data["path"]
        self.contents   = self.data["object"]
        self.language   = self.contents.splitlines()[0]
        self.namespace = {}
    
    def init_param(self, properties):
        if self.scriptpath and self.data.get("lang","ekl").lower() != "plaintext":
            script_glb           = locals()
            script_glb["engine"] = engine
            for i in properties:
                script_glb[i]    = properties[i]
            
            script_contents      = self.contents
            exec(script_contents, globals=script_glb,locals=script_glb)
            self.namespace       = script_glb
    
    def _init_script(self):
        pass
    
    def serialize(self, path):
        # Save the resource into a file
        with open(path, "wb") as f:
            f.write(b"SCR")
            f.write(struct.pack("<I", len(self.get())))
            f.write(self.get().encode())
    
## Functions
def img_to_sheet(img, clip = 0):
    """Convert a spritesheet image to only a part of it."""
    paran = img.data.copy()
    paran["clip"] = clip
    
    ims = SheetImage({
        "data": paran,
        "meta":   {
            "kind": "Resource",
            "name": "SheetImage"
        },
        "script": None
    })

    return ims

## Loader class
class Loader:
    def __init__(self):
        self.game_data     = engine.cvars
        self.save          = engine.savefile
        self.resource_tree = {
            f"Ekl{engine.VER}mem,..unknown": Image({
                "prop":   {},
                "data":   {
                    "object": pg.image.ImageData(
                        25, 25,
                        'RGB',
                        bytes([0, 0, 0] * 25 * 25)
                    ),
                    "path":   f"mem://unknown"
                },
                "meta":   {
                    "kind": "Resource",
                    "name": "Image"
                },
                "script": None
            })
        }
    
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
                dal = struct.unpack("<I", f.read(4))[0] # Data length
                dat = f.read(dal).decode()
                obj = Script({
                    "prop":   {},
                    "data":   {
                        "object": dat,
                        "path":   "res://"
                    },
                    "meta":   {
                        "kind": "Resource",
                        "name": "Script/PlainText"
                    },
                    "script": None
                })
            if type == b"RES":
                obj = Resource({
                    "prop":   {},
                    "data":   {
                        "object": None,
                        "path":   "res://"
                    },
                    "meta":   {
                        "kind": "Resource",
                        "name": "Resource"
                    },
                    "script": None
                })
            if type == b"THM":
                # Themed types:
                #  - Button
                #  - Progressbar
                #  - Treeview
                #  - Label
                
                amoftyp = struct.unpack("<I", f.read(4))
                typ     = struct.unpack(f"<{'I'*amoftyp}", f.read(amoftyp*4))
                
            if type == b"IMG":
                w,h = struct.unpack("<II", f.read(8))
                dal = struct.unpack("<I", f.read(4))[0] # Data length
                dat = f.read(dal).decode()
                obj = Image({
                    "prop":   {},
                    "data":   {
                        "object": self.load(dat).get(),
                        "path":   dat
                    },
                    "meta":   {
                        "kind": "Resource",
                        "name": "Image"
                    },
                    "script": None
                })
            if type == b"IMS":
                w,h      = struct.unpack("<II", f.read(8))   
                cx, cy   = struct.unpack("<II", f.read(8))

                clip     = [cx,cy,w,h]
                if clip == [0,0,0,0]:
                    clip = 0
                
                dal      = struct.unpack("<I", f.read(4))[0]    # Data length
                dat      = f.read(dal).decode()
                obj      = SheetImage({
                    "prop":   {},
                    "data":   {
                        "object": self.load(dat).get(),
                        "path":   dat,
                        "clip":   clip
                    },
                    "meta":   {
                        "kind": "Resource",
                        "name": "Image"
                    },
                    "script": None
                })
        
        return obj
    
    def load(self, path, can_cache=1, force_type = None, return_identifier = False):
        ## Load a resource. Specify path "`user://..`", "`res://..`" or `root://..`"
        ## User:// = save directory
        ## Res://  = project directory
        ## Root:// = directory that the binary is in

        asset       = 0
        typeres     = "mem"
        location    = f"Ekl{engine.VER}{path}".replace('/','.').replace(':',',')
        actual_path = location
        name        = path.split("/")[-1].split(".")[0]
        ext         = path.split(".")[-1].lower()
        if force_type:
            ext = force_type
        if can_cache:
            if location in self.resource_tree:
                asset = self.resource_tree[location]
                return asset
            else:
                print(f"  ~ Loading file {path}")
                if path.startswith("root://"):
                    actual_path = path.lstrip("root://")
                elif path.startswith("user://"):
                    actual_path = self.save + path.lstrip("user://")
                elif path.startswith("res://"):
                    actual_path = self.game_data.get("directory") + "/" + path.lstrip("res://")
                else:
                    actual_path = path
                try:
                    if IS_EXECUTABLE:
                        if ext in ("png","jpg","jpeg","webp","bmp"):
                            asset    = pg.resource.image(actual_path)
                            assetres = Image({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Image"
                                },
                                "script": None
                            })
                        elif ext in ("ttf","otf"):
                            asset    = pg.resource.add_font(actual_path)
                            assetres = Media({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Media"
                                },
                                "script": None
                            })
                        elif ext in ("mp3","ogg","wav","mp4","webm","flac","avi","mpeg"):
                            asset    = Sound(f"{sys._MEIPASS}/{actual_path}")
                            assetres = Media({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Media"
                                },
                                "script": None
                            })
                        elif ext in ("res", "import"):
                            asset    = pg.resource.file(actual_path, "rb")
                            assetres = self.load_from_resf(asset)
                        elif ext in ("ekl", "py", "scn"):
                            asset    = pg.resource.file(actual_path).read()
                            assetres = Script({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "lang":   "python/ekl",
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Script/PlainText"
                                },
                                "script": None
                            })
                        elif ext == "bin":
                            asset    = pg.resource.file(actual_path, "rb").read()
                            assetres = asset
                        else:
                            asset    = pg.resource.file(actual_path, "r").read()
                            assetres = asset
                    else:
                        if ext in ("png","jpg","jpeg","webp","bmp","dds"):
                            asset    = pg.image.load(actual_path)
                            assetres = Image({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Image"
                                },
                                "script": None
                            })
                        elif ext in ("ttf","otf"):
                            asset    = pg.font.load(name)
                            assetres = Media({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Media"
                                },
                                "script": None
                            })
                        elif ext in ("mp3","ogg","wav","mp4","webm","avi","mpeg"):
                            asset    = Sound(actual_path)
                            assetres = Media({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Media"
                                },
                                "script": None
                            })
                        elif ext in ("res", "import"):
                            asset    = open(actual_path,"rb")
                            assetres = self.load_from_resf(asset)
                        elif ext in ("ekl", "py", "scn"):
                            asset    = open(actual_path).read()
                            assetres = Script({
                                "prop":   {},
                                "data":   {
                                    "object": asset,
                                    "lang":   "python/ekl",
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Script/PlainText"
                                },
                                "script": None
                            })
                        elif ext == "bin":
                            asset    = open(actual_path, "rb").read()
                            assetres = asset
                        else:
                            asset    = open(actual_path).read()
                            assetres = asset
                except:
                    if ext == "bin":
                        assetres = b"Faulty"
                    elif ext in ("png","jpg","jpeg","webp","bmp","dds"):
                        assetres = self.resource_tree[f"Ekl{engine.VER}mem,..unknown"]
                    elif ext in ("res", "import"):
                        asset    = io.BytesIO(b"RES")
                        assetres = self.load_from_resf(asset)
                    elif ext in ("ekl", "py", "scn"):
                        asset    = "# Faulty"
                        assetres = Script({
                            "prop":   {},
                            "data":   {
                                "object": asset,
                                    "lang":   "python/ekl",
                                    "path":   path
                                },
                                "meta":   {
                                    "kind": "Resource",
                                    "name": "Script/PlainText"
                                },
                                "script": None
                            })
                    else:
                        assetres = "Faulty"                
                self.resource_tree[location] = assetres
                if return_identifier:
                    return assetres, location
                return assetres