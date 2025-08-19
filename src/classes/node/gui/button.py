## Import inherited
from classes.node.gui.color_rect import ColorRect

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
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
        clicked  = engine.mpressed[0]            

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