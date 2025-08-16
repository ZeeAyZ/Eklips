## Import inherited
from classes.node.node import Node

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as singleton

## Node
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