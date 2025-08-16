## Import all the libraries necessary and engine singleton
import pyglet as pg
from tkinter.messagebox import *
from classes.Object import Object
from anytree import NodeMixin
import classes.Singleton as singleton

## Node
class Node(Object, NodeMixin):
    """
    ## An empty Node.

    Nodes are the building block of Eklips (well, Eklips 4+ atleast). Every Node is inherited off this node class.
    A tree of Nodes make a Scene, A node is stored as `myself.scene` or `scene`.

    All Nodes must have an unique name.
    
    You can make a script have an `_onready(self)` function. This will only run when a Node is fully loaded.
    You can make a script have an `_process(self, delta)` function. This will run every frame after `on_ready()`. The argument `delta` is the delta time variable.
    
    The `self` value in these functions is.. the node the script is attached to. You cannot replace Node functions with a script.

    There is nothing to do with it. The only useful thing to do with it is run a script with it, and no more.
    """
    
    node_base_data = {
        "prop":   {},
        "data":   {},
        "meta":   {
            "kind": "Node",
            "name": "Node"
        },
        "script": None
    }

    def __init__(self, data=node_base_data, parent=None):
        self.parent      = parent
        self.screen      = singleton.interface
        self.resourceman = singleton.resource_loader
        self.window_id   = singleton.interface.main_surf_id
        super().__init__(data)

    def update(self, delta):
        self._process(delta)