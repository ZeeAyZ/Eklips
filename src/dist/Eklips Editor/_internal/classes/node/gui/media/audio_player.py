## Import inherited
from classes.node.node import Node

## Import engine singleton and others
import pyglet as pg
import pygame as pyg
import classes.Singleton as engine

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
            "autostart":   False
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

        self.audio_data   = None
        self.is_playedyet = 0
    
    def play(self, volume=1):
        self.call("_player_started")
        if not self.audio_data:
            self.audio_data = self.resourceman.load(self.properties["media"]).get()
        self.audio_data.set_volume(volume)
        self.audio_data.play()

    def pause(self):
        self.call("_player_paused")
        self.player.pause()
    
    def update(self, delta):
        if not self.is_playedyet and self.properties["autostart"]:
            self.play()
            self.is_playedyet = 1
        
        super().update(delta)