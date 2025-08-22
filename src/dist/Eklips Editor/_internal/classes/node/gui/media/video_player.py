## Import inherited
from classes.node.gui.canvasitem         import CanvasItem
from classes.node.gui.media.audio_player import AudioPlayer

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine
from classes import Resources

## Node
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