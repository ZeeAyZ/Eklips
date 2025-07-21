## Import all the libraries
import pyglet as pg
from classes import UI, Save, Event, Signals, Nodes, Resources
from classes.key_entries import key_entries
from classes.data_ekl import *

shared_console_text = []
def printf(*args):
    args_str = []
    for i in args:
        args_str.append(str(i))
    arg=" ".join(args_str)
    print(arg)
    shared_console_text.append(arg)

class ConHost:
    """ConHost class. Used to handle console output and input."""

    def __init__(self, ui: UI.Interface):
        global shared_console_text
        self.console_text = shared_console_text
        self.ui           = ui
        self.h            = self.ui.screen.height / 2
        self.w            = self.ui.screen.width
        self.y            = -self.h
        self.showing      = False
        self.hiding       = False
        self.speed        = 275
        self.con_panel    = pg.shapes.Rectangle(
            x=0,
            y=self.y,
            width=self.w,
            height=self.h,
            color=(0,0,0,127),
            batch=self.ui.batch
        )
    
    def toggle(self):
        """Toggle the console visibility."""
        print(self.y)
        if self.y == 0:
            self.hiding  = True 
            self.showing = False
        if self.y == -self.h:
            self.showing = True 
            self.hiding  = False
    
    def show(self):
        """Show the console."""
        self.showing = True
    
    def hide(self):
        """Hide the console."""
        self.hiding  = True
    
    def update(self):
        """Update the console."""
        if self.y > 0:
            self.y = 0
        elif self.y < -self.h:
            self.y = -self.h
        if self.showing:
            if self.y < 0:
                self.y += self.ui.delta * self.speed
            else:
                self.showing = False
        elif self.hiding:
            if self.y < -self.h:
                self.y -= self.ui.delta * self.speed
            else:
                self.hiding = False
        
        if self.y > -self.h:
            self.con_panel.y = self.ui.screen.get_size()[1] - self.h - self.y
            self.con_panel.draw()

            if True:
                self.ui.render(
                    "".join(self.console_text),
                    [10,self.y],
                    "main",
                    15,
                    ""
                )
        