## Import inherited
from classes.node.node import Node

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
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
        mpos = engine.mpos
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
            if engine.mpressed[0]:
                self.call("_clicked")

        # World-space relative position
        self.runtime_data["relativepos"] = rel_pos
        self.runtime_data["rendererpos"] = rel_pos
        
        super().update(delta)