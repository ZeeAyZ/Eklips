## Import inherited
from classes.node.twod.node2d import Node2D

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as engine

## Node
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
                    self._handle_bump_y(bounce_mode)
                elif (self.properties["transform"]["pos"][0] + self.w > node.properties["transform"]["pos"][0] and
                      self.properties["transform"]["pos"][0] < node.properties["transform"]["pos"][0] + node.w):
                    self._onw = True
                    # Ow
                    self._handle_bump_x(bounce_mode)
        
        self._handle_motion(bounce_mode)
    
    def _handle_motion(self, bounce_mode=False):
        self.properties["transform"]["pos"][0] += self.motion[0]
        self.properties["transform"]["pos"][1] += self.motion[1]
        
        self._handle_motion_end(bounce_mode)
    
    def _handle_motion_end(self, bounce_mode): # visual
        pass
    
    def _handle_bump_x(self, bounce_mode): # visual
        pass
    
    def _handle_bump_y(self, bounce_mode): # visual
        pass