## Import inherited
from classes.node.twod.physicsbody2d import PhysicsBody2D
from classes.node.gui.canvasitem import CanvasItem

## Import engine singleton and others
import pyglet as pg
import classes.Singleton as singleton

## Node
class Area2D(PhysicsBody2D):
    """
    ## An Area node.
    
    This node has a rectangular hitbox, which won't stop if collided with any bodies. Useful for things like triggers.
    """

    def _check_overlap(self, rect1, rect2):
        # Use AABB
        return (
            rect1.properties["transform"]["pos"][0] < rect2.properties["transform"]["pos"][0] + rect2.properties["transform"]["size"][0] and
            rect1.properties["transform"]["pos"][0] + rect1.properties["transform"]["size"][0] > rect2.properties["transform"]["pos"][0] and
            rect1.properties["transform"]["pos"][1] < rect2.properties["transform"]["pos"][1] + rect2.properties["transform"]["size"][1] and
            rect1.properties["transform"]["pos"][1] + rect1.properties["transform"]["size"][1] > rect2.properties["transform"]["pos"][1]
        )

    def __init__(self, data=CanvasItem.node_base_data, parent=None):
        super().__init__(data,parent)
        self._phys_init()
        self.remap_dim()
        self.id                             = f"{self.to_string()}NodeColA{self.w*self.h}"
        self.scene.nodes_collision[self.id] = self
    
    def remap_dim(self):
        self.x,self.y,self.w,self.h = self.properties["transform"]["pos"][0], self.properties["transform"]["pos"][1], self.properties["transform"]["size"][0], self.properties["transform"]["size"][1]
    
    def colliderect(self, rect): return self._check_overlap(self, rect)

    def collidelist(self, rect_list):
        id = 0
        for i in rect_list:
            if self._check_overlap(self, i): return id
            else: id+=1
        return -1

    def collidelistall(self, rect_list):
        il = []
        for i in rect_list:
            if self._check_overlap(self, i): il.append(i)
        return il
    
    def get_all_rects_nearby(self, rang=500):
        il = []
        for i in self.scene.nodes_collision:
            node = self.scene.nodes_collision[i]
            # rang = The range in pixels that this rectangle can be in to count

            if node == self: continue

            if abs(node.x - node.x) < rang:
                if abs(node.y - node.y) < rang:
                    il.append(node)
        return il
    
    def update(self, delta):
        super().update(delta)

        self.remap_dim()
        nearby   = self.get_all_rects_nearby()
        collided = self.collidelistall(nearby)
        self._physics_update(nearby, collided)  # Update physics based on nearby rectangles and collided ones

    def free(self):
        self.scene.nodes_collision.pop(self.id)
        super().free()