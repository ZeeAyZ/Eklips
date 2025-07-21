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
        self.shown        = False
        self.ui           = ui
        self.h            = self.ui.screen.height / 2
        self.w            = self.ui.screen.width
        self.y            = -self.h
        self.showing      = False
        self.hiding       = False
        self.blink_timer  = 0
        self.speed        = 275.5
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
        if not (self.showing or self.hiding):
            self.shown = not self.shown

            if self.shown:
                self.show()
            else:
                self.hide()
    
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
            if self.y > -self.h:
                self.y -= self.ui.delta * self.speed
            else:
                self.hiding = False
        
        if self.y > -self.h:
            self.con_panel.y = self.ui.screen.get_size()[1] - self.h - self.y
            self.con_panel.draw()
            
            if len(self.console_text) > (self.h/35)-1:
                self.console_text.pop(0)
        
            con_y = self.y
            for i in self.console_text:
                self.ui.render(
                    i,
                    [10,con_y],
                    "main",
                    15,
                    ""
                )
                con_y += 35
            
            blk_g = " "
            if self.blink_timer > 1:
                blk_g = "_"
            if self.blink_timer > 2:
                self.blink_timer = 0
            self.blink_timer += self.ui.delta * 5

            self.ui.render(f"] {None}{blk_g}", [5,self.y+self.h-35], "main", 15)
        
    def input(self, text):
        """Input text to the console."""
        if text:
            self.console_text.append(text)