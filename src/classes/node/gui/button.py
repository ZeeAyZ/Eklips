## Import inherited
from classes.node.gui.canvasitem import CanvasItem

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
class Button(CanvasItem):
    node_base_data = {
        "prop":   {
            "transform": {
                "pos":    [0,0],
                "anchor": "top left",
                "layer":  0,
                "alpha":  1,
                "size":   [100, 100],
                "scroll": [0, 0],
                "rot":    0
            },
            "visible": True,
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

        if not self.holding:
            self.draw()
        else:
            self.draw("pbutton")
    
    def draw(self, typ="button"):
        if self.properties["visible"]:
            self.w,self.h = self._draw_onto_screen(typ)
    
    def _draw_onto_screen(self, typ="button"):
        lbl = self.screen.render(
            self.properties["text"],
            [
                self.runtime_data["rendererpos"][0]+7.5,
                self.runtime_data["rendererpos"][1]
            ],
            anchor = self.properties["transform"]["anchor"],
            color  = engine.thm.get_thing(typ)["fontcol"]
        )

        # Check if size property is smaller than it should be
        sz     = self.properties["transform"]["size"]
        if sz[0] < lbl[0]:
            sz[0] = lbl[0]+(engine.thm.get_thing(typ)["margin"]*5)
        if sz[1] < lbl[1]:
            sz[1] = lbl[1]+7.5

        # Draw the themed button        
        thmobj = engine.thm.draw_marginable_thing(typ, self.runtime_data["rendererpos"], sz, self.window_id, self.properties["transform"]["anchor"], self.properties["transform"]["layer"])
        return thmobj