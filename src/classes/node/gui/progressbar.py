## Import inherited
from classes.node.gui.canvasitem import CanvasItem

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as singleton
from classes import Resources

class Progressbar(CanvasItem):
    """
    ## A Canvas Node to render a colored Progressbar.
     
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
            "bgcolor": [128, 128, 128],
            "fgcolor": [128, 0,   0  ],
            "txcolor": [255, 255, 255],

            "minimum": 0,
            "maximum": 100,
            "value":   50
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
        
        r, g, b = self.properties["bgcolor"]
        raw_data = bytes([r, g, b] * self.properties["transform"]["size"][0] * self.properties["transform"]["size"][1])
        self.bg_img = Resources.Image(
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
        
        r, g, b = self.properties["fgcolor"]
        raw_data = bytes([r, g, b] * 1 * self.properties["transform"]["size"][1])
        self.fg_img = Resources.Image(
            {
                "prop":   {},
                "data":   {
                    "object": pg.image.ImageData(
                        1,
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
    
    def draw(self):
        if self.bg_img and self.properties["visible"]:
            self.w,self.h=self.bg_img.width,self.bg_img.height
            self._draw_onto_screen(self.bg_img, self.fg_img, int(self.properties["transform"]["size"][0] * (self.properties["value"] / abs(self.properties["maximum"] - self.properties["minimum"]))))
    
    def _draw_onto_screen(self, img, fg, width):
        bg = self.screen.blit(
            img,                                   
            self.runtime_data["rendererpos"],             
            anchor  = self.properties["transform"]["anchor"],
            scale   = self.properties["transform"]["scale"],
            layer   = self.properties["transform"]["layer"],
            rot     = self.properties["transform"]["rot"],
            opacity = self.properties["transform"]["alpha"],
            scroll  = self.properties["transform"]["scroll"]
        )

        self.screen.blit(
            fg,                                   
            self.runtime_data["rendererpos"],             
            anchor  = self.properties["transform"]["anchor"],
            scale   = [
                width * self.properties["transform"]["scale"][0],
                self.properties["transform"]["scale"][1]
            ],
            layer   = self.properties["transform"]["layer"],
            rot     = self.properties["transform"]["rot"],
            opacity = self.properties["transform"]["alpha"],
            scroll  = self.properties["transform"]["scroll"]
        )

        self.screen.render(
            f"{round(self.properties['value']/self.properties['maximum'])*100}%",
            [
                self.runtime_data["rendererpos"][0],
                self.runtime_data["rendererpos"][1]
            ],                     
            anchor = self.properties["transform"]["anchor"],              
            layer  = self.properties["transform"]["layer"],       
            color  = self.properties.get("txcolor", [255,255,255])
        )

        return bg

    def update(self, delta):
        super().update(delta)
        self.draw()    