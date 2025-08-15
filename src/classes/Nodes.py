## Import all the libraries
import pyglet as pg
import json, time, types, tkinter as tk
from tkinter.messagebox import *
from classes import Event, UI, Resources
from classes.Resources import Object
from pyglet import gl
from anytree import NodeMixin
from PIL import Image, ImageTk
import classes.singleton as singleton

## Scene class
class Scene:
    def __init__(self, file_path):
        self.file_path        = file_path
        self.nodes            = {}
        self.cam_pos          = [0, 0]
        self.nodes_collision  = {}
        self.properties       = {}
        self.screen           = singleton.interface
        self.resourceman      = singleton.resource_loader
    
    def empty(self):
        self.nodes_collision = {}
        self.cam_pos         = [0, 0]
        for i in self.nodes:
            self.nodes[i]["object"].free()
        self.nodes           = {}
    
    def add_node(self, node_data={}):
        id = len(self.nodes)

        # Full path including this node
        full_path   = f"{node_data['path']}/{node_data['name']}".strip("/")

        directories  = full_path.split("/")[:-1]  # Only parents, exclude self
        parent       = None
        current_path = ""

        for directory in directories:
            if len(current_path) == 0:
                continue
            existing = self.get_node_from_path(current_path.lstrip("/"), directory)
            current_path += f"/{directory}"
            if not existing:
                raise Exception("The parent of the node you are creating does not exist.")
            else:
                parent = existing

        # Construct node data
        node_obj_data = {
            "prop":   node_data["properties"],
            "data":   {},
            "meta":   {
                "kind": "Node",
                "name": node_data["name"]
            },
            "script": node_data["script"]
        }

        # Create the actual node
        classobj           = globals().get(node_data["type"])
        object             = classobj.__new__(classobj)
        object.__init__(node_obj_data, parent)

        # Store in flat dictionary
        self.nodes[id] = {
            "class": node_data["type"],
            "path": node_data["path"],
            "object": object,
            "name": node_data["name"],
            "base_data": node_data
        }

        return self.nodes[id]["object"]

    def load(self):
        self.empty()
        scene_obj  = json.loads(self.resourceman.load(self.file_path).get())
        self.properties = scene_obj["Properties"]
        for node in scene_obj["Nodes"]:
            node_data = scene_obj["Nodes"][node]
            self.add_node(node_data)

    def update(self, delta):
        try:
            for nodeID in self.nodes:
                node            = self.nodes[nodeID]["object"]

                if node.stop_running:
                    node._free()
                    continue
                node.update(delta)
        except Exception as error:
            print(f" Scene({self.file_path}) had an error updating; {error}")
            raise error
    
    ## Get nodes
    def get_node_from_path(self, path, name):
        for i in self.nodes:
            if self.nodes[i]["path"] == path:
                if self.nodes[i]["name"] == name:
                    return self.nodes[i]["object"]

## Nodes (ROOT NODES)
class Node(Object, NodeMixin):
    """
    ## An empty Node.

    Nodes are the building block of Eklips (well, Eklips 4+ atleast). Every Node is inherited off this node class.
    A tree of Nodes make a Scene, A node is stored as `myself.scene` or `scene`.

    All Nodes must have an unique name.
    
    You can make a script have an `_onready(self)` function. This will only run when a Node is fully loaded.
    You can make a script have an `_process(self, delta)` function. This will run every frame after `on_ready()`. The argument `delta` is the delta time variable.
    
    The `self` value in these functions is.. the node the script is attached to. You cannot replace Node functions with a script.

    There is nothing to do with it. The only useful thing to do with it is run a script with it, and no more.
    """
    
    node_base_data = {
        "prop":   {},
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        self.parent      = parent
        self.screen      = singleton.interface
        self.resourceman = singleton.resource_loader
        self.window_id   = singleton.interface.main_surf_id
        super().__init__(data)

    def update(self, delta):
        self._process(delta)

class TkWindow(Node):
    """
    ## A Tkinter Window.

    Self-explanatory if you have used Tkinter. `TkWindow.tk_self` is the Tk() object.
    No 2D Nodes work in this. The icon property only works if the image isn't a part of the executable.
    """
    
    node_base_data = {
        "prop":   {
            "caption":     "Node.Window.Tk",
            "icon":        None,
            "dimension":   "640x480"
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.tk_self = tk.Tk()
        self.tk_self.geometry(self.properties["dimension"])
        self.tk_self.title(self.properties["caption"])
        icon_image  = Image.open(self.properties["icon"].replace("res://", self.project_data.data_directory+"/"))
        photo_image = ImageTk.PhotoImage(icon_image)
        self.tk_self.wm_iconphoto(True, photo_image)

class OptionDialog(Node):
    """
    ## A Window node to ask for a question.
     
    The `OptionDialog.fate` value is a boolean, It returns True if the user chose an affirmative values.

    The questions that can be asked are:
    # 1: Yes/No
    # 2: Ok/Cancel
    # 3: Retry/Cancel
    # 4: Yes/No/Cancel
    """

    node_base_data = {
        "prop":   {
            "caption":     "Node.Window.Tk.Dialog",
            "message":     "Node.Window.Tk.Dialog.Message",
            "optionindex": 4
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.fate = None
    
    def popup(self):
        if self.properties["optionindex"] == 1:
            func=askyesno(self.properties["caption"], self.properties["message"])
        if self.properties["optionindex"] == 2:
            func=askokcancel(self.properties["caption"], self.properties["message"])
        if self.properties["optionindex"] == 3:
            func=askretrycancel(self.properties["caption"], self.properties["message"])
        if self.properties["optionindex"] == 4:
            func=askyesnocancel(self.properties["caption"], self.properties["message"])
        self.call("_popup_answer", func)

class AudioPlayer(Node):
    """
    ## A Media Node to play audio.
     
    Self-explanatory.
    """
    
    node_base_data = {
        "prop":   {
            "media":       "res://media/load.mp3",
            "loop":        False,
            "autostart":   False,
            "play_global": False
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        global player_global
        super().__init__(data,parent)

        if self.properties["play_global"]:
            self.player = singleton.global_stream
        else:
            self.player = pg.media.Player()

        self.audio_data   = 0
        self.is_playedyet = 0
    
    def play(self, volume=1):
        self.call("_player_started")
        what = self.audio_data
        if not what:
            what = self.resourceman.load(self.properties["media"]).get()
        self.player.queue(what)
        self.player.volume = volume
        self.player.play()

    def pause(self):
        self.call("_player_paused")
        self.player.pause()
    
    def update(self, delta):
        if not self.is_playedyet and self.properties["autostart"]:
            self.play()
            self.is_playedyet = 1
        
        super().update(delta)

class CanvasItem(Node):
    """
    ## A Canvas Node.
    
    This is a Node that has properties for transformation, and is meant for rendering items in the window.
    This has no properties for Cameras, which makes it good for rendering UI elements. Which is it's purpose.
    For Nodes in a 2D world, use Node2D.

    This has relativity only on the position and anchor.
    """
    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible": True,
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.w,self.h                    = 0, 0
        self.anchor                      = self.properties["transform"]["anchor"]
        self.runtime_data["rendererpos"] = self.properties["transform"]["pos"][:]
        self.runtime_data["relativepos"] = self.properties["transform"]["pos"][:]

    def get_relative_pos(self):
        my_pos     = self.properties["transform"]["pos"]
        parent_pos = [0, 0]
        if self.parent and hasattr(self.parent, "get_relative_pos"):
            parent_pos = self.parent.get_relative_pos()[0]
            return [my_pos[0] + parent_pos[0], my_pos[1] + parent_pos[1]], parent_pos
        return my_pos[:], parent_pos
    
    def get_relative_anchor(self):
        if self.parent and hasattr(self.parent, "anchor"):
            return self.parent.properties["transform"]["anchor"]
        return self.properties["transform"]["anchor"]
    
    def draw(self):
        if self.image and self.properties["visible"]:
            self.w,self.h=self.image.width,self.image.height
            self._draw_onto_screen(self.image)
    
    def get_if_mouse_hovering(self):
        mpos = singleton.mpos
        return (
            mpos[0] < self.properties["transform"]["pos"][0] + self.w and
            mpos[0] + 20 > self.properties["transform"]["pos"][0]     and
            mpos[1] < self.properties["transform"]["pos"][1] + self.h and
            mpos[1] + 20 > self.properties["transform"]["pos"][1]
        )
    
    def _draw_onto_screen(self, img):
        return self.screen.blit(
            img,                                   
            self.runtime_data["rendererpos"],             
            anchor  = self.properties["transform"]["anchor"],
            scale   = self.properties["transform"]["scale"],
            layer   = self.properties["transform"]["layer"],
            rot     = self.properties["transform"]["rot"],
            opacity = self.properties["transform"]["alpha"],
            scroll  = self.properties["transform"]["scroll"]
        )
        
    def update(self, delta):
        self.anchor                      = self.properties["transform"]["anchor"]
        rel_pos, parent_pos              = self.get_relative_pos()

        if self.get_if_mouse_hovering():
            self.call("_hover")
            if singleton.mpressed[0]:
                self.call("_clicked")

        # World-space relative position
        self.runtime_data["relativepos"] = rel_pos
        self.runtime_data["rendererpos"] = rel_pos
        
        super().update(delta)

class VideoPlayer(CanvasItem, AudioPlayer):
    """
    ## A Media Node to render video and play it's audio.
     
    Self-explanatory.
    """

    node_base_data = {
        "prop":   {
            "media":       "res://media/load.mp3",
            "loop":        False,
            "where":       0,
            "autostart":   False,

            "transform":  {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "scroll": [0,0]
            }
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        global player_global
        super().__init__(data,parent)

        self.audio_data   = 0
        self.as_playedyet = 0

        self.runtime_data["rendererpos"] = self.properties["transform"]["pos"]
    
    def update(self, delta):
        global camera_pos
        super().update(delta)
        
        if self.player.playing:
            self.draw(
                Resources.Image(
                    {
                        "prop":   {},
                        "data":   {
                            "object": self.player.texture,
                            "path":   f"player{self.properties['media']}"
                        },
                        "meta":   {
                            "kind": "Resource",
                            "name": "Media"
                        },
                        "script": None
                    }
                )
            )
    
class Timer(Node):
    """
    ## A Timer.

    It's a fucking timer??
    """

    node_base_data = {
        "prop":   {
            "duration_ep": 0,          # in seconds
            "only_once":   False,
            "autostart":   False,
            "play_global": False
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        global player_global
        super().__init__(data,parent)
        self.is_playedyet  = False
        self.playing       = False       #... is timing?
        self.start_epoch   = time.time() #what the epoch was when timer started
        self.current_epoch = time.time() #current time
    
    def start(self):
        self.start_epoch = time.time()
        self.playing     = True
    
    def get_time_since_start(self):
        return self.current_epoch-self.start_epoch
    
    def format_time(self, epoch_time):
        """Format an epoch timestamp in seconds"""
        return float(f"{epoch_time:.6f}".lstrip("-"))
    
    def stop(self): self.playing = False

    def update(self, delta):
        super().update(delta)
        self.current_epoch = time.time()
        if not self.is_playedyet and self.properties["autostart"]:
            self.start()
            self.is_playedyet=True
        if self.playing:
            if self.get_time_since_start()>self.properties["duration"]:
                self.stop()

class Node2D(CanvasItem):
    """
    ## A 2D Node.
    
    This is basically the same as a CanvasItem, but meant for gameplay purposes, because it follows the camera.
    All nodes that are meant in a 2D space (Camera2D, Sprite2D..) are inherited from this Node.
    """
    
    def update(self, delta):
        global camera_pos
        self.anchor                      = self.properties["transform"]["anchor"]
        rel_pos, parent_pos              = self.get_relative_pos()

        # World-space relative position
        self.runtime_data["relativepos"] = rel_pos
        cam = self.scene.cam_pos
        self.runtime_data["rendererpos"] = [rel_pos[0] - cam[0], rel_pos[1] - cam[1]]
        
        super().update(delta)

## Every canvas node
class Label(CanvasItem):
    """
    ## A Canvas Node to render text.
     
    Self-explanatory.
    """
    
    node_base_data = {
        "prop":   {
            "transform": {
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "rot":    0
            },
            "visible": True,
            "text":    "",
            "color":   [255,255,255]
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def draw(self):
        if self.properties["visible"]:
            pos = self.runtime_data["rendererpos"]
            self.w,self.h=self._draw_onto_screen(pos)
        
    def _draw_onto_screen(self, pos):
        return self.screen.render(
            text    = self.properties["text"],
            pos     = pos,

            anchor  = self.anchor,
            layer   = self.properties["transform"]["layer"],
            blit_in = self.window_id,
            size    = self.properties["font_size"],
            rot     = self.properties["transform"]["rot"],
            alpha   = self.properties["transform"]["alpha"],
            color   = self.properties["color"]
        )
    
    def update(self, delta):
        super().update(delta)
        self.draw()

class ColorRect(CanvasItem):
    """
    ## A Canvas Node to render a colored Rectangle.
     
    Self-explanatory.
    """
     
    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible": True,
            "color":   [128, 128, 128]
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        r, g, b = self.properties["color"]
        # RGB for each pixel, repeated for all pixels
        raw_data = bytes([r, g, b] * self.properties["transform"]["size"][0] * self.properties["transform"]["size"][1])
        self.image = Resources.Image(
            {
                "prop":   {},
                "data":   {
                    "object": pg.image.ImageData(
                        self.properties["transform"]["size"][0],
                        self.properties["transform"]["size"][1],
                        'RGB',
                        raw_data
                    ),
                    "path":   f"{r}{g}{b}{self.properties["transform"]["size"]}.mm"
                },
                "meta":   {
                    "kind": "Resource",
                    "name": "Image"
                },
                "script": None
            }
        )

    def update(self, delta):
        super().update(delta)
        self.draw()

class Button(ColorRect):
    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible": True,
            "color":   [128, 128, 128],
            "text":    "Text"
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }


    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.clicked             = False
        self.image               = 0
    
    def update(self, delta):
        super().update(delta)
        hovering = self.get_if_mouse_hovering()
        clicked  = singleton.mpressed[0]            

        self.clicked = (hovering and clicked)

        if not self.clicked:
            self.draw()
    
    def _draw_onto_screen(self, img):
        self.screen.render(
            self.properties["text"],
            [
                self.runtime_data["rendererpos"][0]+7.5,
                self.runtime_data["rendererpos"][1]
            ],
            anchor=self.properties["transform"]["anchor"],
            size = self.properties["font_size"]
        )
        return super()._draw_onto_screen(img)

class Treeview(CanvasItem):
    # TODO: Make visually pleasing
    node_base_data = {
        "prop":   {
            "transform": {
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0
            },
            "visible":  True,
            "children": {}
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.treechildren = {}
        self.revealed     = []
    
    def _rlayer(self, data, pos=[0,0], layer = 0):
        id        = 0
        _pos      = pos.copy()
        for i in data:
            node_p    = f"{self.node_path_da}/{self.name}"
            nm        = f"Label{id}"
            _have_kid = "v " if len(data[i]) else ""
            self.screen.render(
                text    = f"{'| '*layer}{_have_kid}{i}",
                pos     = _pos,
                anchor  = "",
                layer   = 10+id,
                blit_in = self.window_id
            )
            id      += 1
            _pos[1] += 25
            _pos     = self._rlayer(data[i], _pos, layer+1)
        return _pos

    def update(self, delta):
        super().update(delta)
        # TBA
        self.treechildren = self.properties["children"]
        self.revealed     = []
        
        if self.properties["visible"]:
            self._rlayer(self.treechildren, self.runtime_data["rendererpos"].copy())

## Every other 2D node
class PhysicsBody2D(Node2D):
    def _phys_init(self):
        self.should_stop = True
        self._onf        = False
        self._onw        = False
        self.weight      = 1
        self.motion      = [0, 0]

    def if_on_floor(self): return self._onf 
    def if_on_wall(self):  return self._onw
    def _physics_update(self, nearby, collided, bounce_mode = False):
        # Most basic of basic physics.
        self._onf = False
        self._onw = False

        for node in collided:
            if self.colliderect(node) and node.get_class() == "Area2D":
                # You little shit
                if self.properties["transform"]["pos"][1] + self.h <= node.properties["transform"]["pos"][1]:
                    self._onf = True
                    # Ow
                    if bounce_mode:
                        self.motion[1] = -self.motion[1] / self.weight
                    else:
                        self.motion[1] = 0
                elif (self.properties["transform"]["pos"][0] + self.w > node.properties["transform"]["pos"][0] and
                      self.properties["transform"]["pos"][0] < node.properties["transform"]["pos"][0] + node.w):
                    self._onw = True
                    print("collided_")
                    # Ow
                    if bounce_mode:
                        self.motion[0] = -self.motion[0] / self.weight
                    else:
                        self.motion[0] = 0
            
        self.properties["transform"]["pos"][0] += self.motion[0]
        self.properties["transform"]["pos"][1] += self.motion[1]
        
        if self.should_stop:
            if bounce_mode:
                self.motion[1] = -self.motion[1]
            else:
                self.motion = [0,0]

class CollisionBox2D(PhysicsBody2D):
    """
    ## A Collision Box.
    
    This node has a rectangular hitbox, which will stop any moving bodies if collided with.
    """

    def _check_overlap(self, rect1, rect2):
        # Use AABB
        return (
            rect1.properties["transform"]["pos"][0] < rect2.properties["transform"]["pos"][0] + rect2.properties["transform"]["size"][0] and
            rect1.properties["transform"]["pos"][0] + rect1.properties["transform"]["size"][0] > rect2.properties["transform"]["pos"][0] and
            rect1.properties["transform"]["pos"][1] < rect2.properties["transform"]["pos"][1] + rect2.properties["transform"]["size"][1] and
            rect1.properties["transform"]["pos"][1] + rect1.properties["transform"]["size"][1] > rect2.properties["transform"]["pos"][1]
        )

    def __init__(self, data=CanvasItem.node_base_data, parent=None):
        super().__init__(data,parent)
        self._phys_init()
        self.remap_dim()
        self.id                             = f"{self.to_string()}NodeColA{self.w*self.h}"
        self.scene.nodes_collision[self.id] = self
    
    def remap_dim(self):
        self.x,self.y,self.w,self.h = self.properties["transform"]["pos"][0], self.properties["transform"]["pos"][1], self.properties["transform"]["size"][0], self.properties["transform"]["size"][1]
    
    def colliderect(self, rect): return self._check_overlap(self, rect)

    def collidelist(self, rect_list):
        id = 0
        for i in rect_list:
            if self._check_overlap(self, i): return id
            else: id+=1
        return -1

    def collidelistall(self, rect_list):
        il = []
        for i in rect_list:
            if self._check_overlap(self, i): il.append(i)
        return il
    
    def get_all_rects_nearby(self, rang=500):
        il = []
        for i in self.scene.nodes_collision:
            node = self.scene.nodes_collision[i]
            # rang = The range in pixels that this rectangle can be in to count

            if node == self: continue

            if abs(node.x - node.x) < rang:
                if abs(node.y - node.y) < rang:
                    il.append(node)
        return il
    
    def update(self, delta):
        super().update(delta)

        self.remap_dim()
        nearby   = self.get_all_rects_nearby()
        collided = self.collidelistall(nearby)
        self._physics_update(nearby, collided)  # Update physics based on nearby rectangles and collided ones

    def free(self):
        self.scene.nodes_collision.pop(self.id)
        super().free()

class Area2D(CollisionBox2D):
    """
    ## An Area node.

    This is the same as a CollisionBox2D node, but it doesn't stop any moving bodies if collided with.
    """
    
    def update(self, delta):
        self.should_stop = False
        super().update(delta)

class Camera2D(Node2D):
    """
    ## A 2D Node to control the Camera in the 2D world.
     
    Self-explanatory. The position of this Node is the position of the camera
    """
    
    def __init__(self, data=Node2D.node_base_data, parent=None):
        super().__init__(data,parent)
        self.target      = None
    
    def follow(self, target_node): self.target = target_node
    
    def update(self, delta):
        super().update(delta)
        if not self.target:
            self.scene.cam_pos = [
                self.properties["transform"]["pos"][0] - self.screen.screen.width  // 2,
                self.properties["transform"]["pos"][1] - self.screen.screen.height // 2
            ]
        else:
            w,h=self.target.w,self.target.h
            self.scene.cam_pos = [
                self.target.properties["transform"]["pos"][0] - self.screen.screen.width  // 2 - w // 2,
                self.target.properties["transform"]["pos"][1] - self.screen.screen.height // 2 - h // 2
            ]

class Sprite2D(Node2D):
    """
    ## A 2D Node to display an image.
     
    Self-explanatory.
    """

    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "scroll": [0, 0],
                "rot":    0
            },
            "visible":  True,
            "sprite":   "res://media/bg.png"
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }
    
    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        asset      = self.resourceman.load(self.properties["sprite"])
        self.image = asset
    
    def update(self, delta):
        super().update(delta)
        self.draw()

class AnimatedSprite2D(Sprite2D):
    """
    ## A 2D Node to display an animmated image.
     
    Self-explanatory.
    """

    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible":  True,
            "sprite":   ["res://media/bg.png"]
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }
    
    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
        self.images      = []
        self.sprite_used = 0          
        for i in self.properties["sprite"]: 
            asset = self.resourceman.load(i)
            self.images.append(asset)       
    
    def draw(self):
        if self.sprite_used in self.images and self.properties["visible"]:
            img=self.images[self.sprite_used]
            self.w,self.h=img.w,img.h
            return self._draw_onto_screen(img)

class Parallax2D(Sprite2D):
    """
    ## A 2D Sprite Node.. to scroll the image at a provided speed..
     
    There is seriously no way you need help with this
    """

    node_base_data = {
        "prop":   {
            "transform": {
                "scale":  [1,1],
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible":      True,
            "sprite":       "res://media/bg.png",
            "scroll_speed": 5,
        },
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }
    
    def __init__(self, data=node_base_data, parent=None):
        super().__init__(data,parent)
    
    def update(self, delta):
        super().update(delta)

        self.properties["transform"]["scroll"][0] -= self.properties["scroll_speed"]
        if self.properties["transform"]["scroll"][0] < (-self.image.get().width) + self.properties["scroll_speed"]:
            self.properties["transform"]["scroll"][0] = -(self.properties["scroll_speed"])
            self.call("_reached_end")