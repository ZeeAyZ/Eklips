## Import inherited
from classes.node.gui.canvasitem import CanvasItem

## Import engine singleton singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
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