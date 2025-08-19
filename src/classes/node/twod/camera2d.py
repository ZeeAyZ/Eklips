## Import inherited
from classes.node.twod.node2d import Node2D

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
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