## Import all the libraries
import pyglet as pg
from classes import UI, CV, convenience
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

    def __init__(self, ui: UI.Interface, cvars: CV.CvarCollection):
        global shared_console_text
        self.cvars        = cvars
        self.console_text = shared_console_text
        self.shown        = False
        self.ui           = ui
        self.input_text   = ""
        self.h            = self.ui.screen.height / 2
        self.w            = self.ui.screen.width
        self.y            = -self.h
        self.showing      = False
        self.hiding       = False
        self.blink_timer  = 0
        self.is_upper     = False
        self.hold_timer   = 0
        self.klp          = None
        self.speed        = 450
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
    
    def update(self, keys_nheld, keys_pressed):
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

            if self.hold_timer > 0.6 and self.klp and self.klp in keys_pressed:
                self._prockey(self.klp)

            if len(keys_nheld) > 0:
                char = keys_nheld[0]
                if char == 8:  # Backspace
                    self.input_text = self.input_text[:-1]
                elif char == pg.window.key.RETURN:  # Enter
                    self.input(self.input_text)
                self._prockey(char)
                self.hold_timer = 0
            
            self.hold_timer += self.ui.delta

            self.ui.render(f"] {self.input_text}{blk_g}", [10,self.y+self.h-35], "main", 15)
    
    def _prockey(self, key):
        """Process a key input."""
        if key == pg.window.key.CAPSLOCK:
            self.is_upper = not self.is_upper
        
        if key == pg.window.key.BACKSPACE:
            self.input_text = self.input_text[:-1]
        elif key == pg.window.key.RETURN:
            self.input(self.input_text)
        elif key in key_entries:
            self.input_text += key_entries[key]
        else:
            
            if key in [pg.window.key.LSHIFT, pg.window.key.RSHIFT] or self.is_upper:
                self.input_text += chr(key).upper() if 0 <= key < 256 else ""
            else:
                self.input_text += chr(key) if 0 <= key < 256 else ""
        self.klp = key
    
    def _proccmd(self, text):
        """Process a command input."""
        data         = text.split(" ")
        if len(data) < 1:
            return
        opc          = data[0].lower()
        try: args    = data[1:]
        except: args = [None]
        if opc.startswith("sv-"):
            cvar = opc.lstrip("sv-")
            if len(args) > 0:
                self.cvars.set(cvar, convenience._turntypeatfirstglance(args[0]))
            printf(f"{cvar} = {self.cvars.get(cvar, 'Undefined')}")
    
    def input(self, text):
        """Input text to the console."""
        if text:
            self.console_text.append(f"] {text}")
            self.input_text = ""
            self.klp        = None
            self.hold_timer = 0
            try:
                self._proccmd(text)
            except Exception as error:
                printf(f"Error processing command '{text}': {error}")