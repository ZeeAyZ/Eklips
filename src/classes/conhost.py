## Import all the libraries
import pyglet as pg
from classes import UI, CV, convenience
from classes.key_entries import key_entries
from classes.constants_ekl import *
import classes.singleton as singleton

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

    def __init__(self):
        global shared_console_text
        self.cvars        = singleton.cvars
        self.data         = singleton.Data
        self.console_text = shared_console_text
        self.shown        = False
        self.ui           = singleton.interface
        self.input_text   = ""
        self.h            = "df"
        self.w            = self.ui.screen.width
        self.y            = None
        self.showing      = False
        self.hiding       = False
        self.blink_timer  = 0
        self.eng_gl       = {}
        self.is_upper     = False
        self.hold_timer   = 0
        self.klp          = None
        self.speed        = self.cvars.get("con_speed")
        self.bl_rate      = self.cvars.get("con_rate")
        self.shifted      = False
        self.ll           = (len(self.ui.layers)//2)-1
        self.mk_panel()
    
    def mk_panel(self):
        self.h     = self.cvars.get("con_size", "df")
        if self.h == "df":
            self.h = self.ui.screen.height // 2
        if self.y == None:
            self.y = -self.h
        self.con_panel    = pg.shapes.Rectangle(
            x=0,
            y=self.y,
            width=self.w,
            height=self.h,
            color=(0,0,0,197),
            group=self.ui.layers[self.ll-1],
            batch=self.ui.batch
        )
    
    def toggle(self):
        """Toggle the console visibility."""
        self.speed   = self.cvars.get("con_speed")
        self.bl_rate = self.cvars.get("con_rate")
        if self.cvars.get("con_size", self.con_panel.width) != self.con_panel.width:
            self.mk_panel()
        
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
    
    def update(self, keys_nheld, keys_pressed, eng_gl):
        self.eng_gl = eng_gl
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
            
            amchirncon=(self.h//25)-1
            if len(self.console_text) > amchirncon:
                for i in range(int(len(self.console_text)-amchirncon)):
                    self.console_text.pop(0)
        
            con_y = self.y
            for i in self.console_text:
                self.ui.render(
                    i,
                    [10,con_y],
                    "main",
                    self.ll,
                    ""
                )
                con_y += 25
            
            blk_g = " "
            if self.blink_timer > 1:
                blk_g = "_"
            if self.blink_timer > 2:
                self.blink_timer = 0
            self.blink_timer += self.ui.delta * self.bl_rate

            if self.hold_timer > 0.6 and self.klp and self.klp in keys_pressed:
                self._prockey(self.klp)

            if len(keys_nheld) > 0:
                char = keys_nheld[0]
                if char   == pg.window.key.BACKSPACE: # Backspace
                    self.input_text = self.input_text[:-1]
                elif char == pg.window.key.RETURN:    # Enter
                    self.input(self.input_text)
                self._prockey(char)
                self.hold_timer = 0
            
            self.hold_timer += self.ui.delta

            self.ui.render(f"] {self.input_text}{blk_g}", [10,self.y+self.h-35], "main", self.ll)
    
    def _prockey(self, key):
        """Process a key input."""
        if key == pg.window.key.CAPSLOCK:
            self.is_upper = not self.is_upper
        if key in [pg.window.key.LSHIFT, pg.window.key.RSHIFT]:
            self.shifted = True
        
        if key == pg.window.key.BACKSPACE:
            self.input_text = self.input_text[:-1]
        elif key == pg.window.key.RETURN:
            self.input(self.input_text)
        elif key in key_entries:
            self.input_text += key_entries[key]
        else:
            if self.shifted: # or self.is_upper:
                nk = convenience._shift_k(chr(key))
                self.input_text += nk if 0 <= key < 256 else ""
                if not key in [pg.window.key.LSHIFT, pg.window.key.RSHIFT]:
                    self.shifted = False
            elif self.is_upper:
                self.input_text += chr(key).upper() if 0 <= key < 256 else ""
            else:
                self.input_text += chr(key) if 0 <= key < 256 else ""
        self.klp = key
    
    def list_cvar(self, name):
        """List a cvar's data."""
        data = self.cvars.get(name, "Undefined")
        desc = self.cvars.get_description(name, "No description")
        printf(f"{name} = {data} :: {desc}")
    
    def _proccmd(self, text):
        """Process a command input."""
        data         = text.split(" ")
        if len(data) < 1:
            return
        opc          = data[0].lower()
        try: args    = data[1:]
        except: args = [None]
        if opc.startswith("sv_"):
            cvar = opc.lstrip("sv_")
            if cvar == "list":
                for cvar_name in self.cvars.cvars:
                    self.list_cvar(cvar_name)
            else:
                if len(args) > 0:
                    self.cvars.set(cvar, convenience._turntypeatfirstglance(args[0]))
                self.list_cvar(cvar)
        elif opc == "eng_chproj":
            exec(f"singleton.Data.project_file = '{args[0]}/game.json'", self.eng_gl, self.eng_gl)
            exec(f"singleton.Data.directory = '{args[0]}'", self.eng_gl, self.eng_gl)
            exec(f"singleton.reload_engine('{args[0]}')", self.eng_gl, self.eng_gl)
        else:
            try:
                g           = self.eng_gl.copy()
                g["args"]   = args
                g["engine"] = singleton
                pline       = self.data.game_bdata["cmd"][opc].splitlines()[0]
                if pline.startswith("@pointer="):
                    pointer_file = pline[9:]
                    exec(singleton.resource_loader.load(pointer_file).get(), g,g)
                else:
                    exec(self.data.game_bdata["cmd"][opc], g,g)
            except Exception as error:
                if opc in self.data.game_bdata["cmd"]:
                    printf(f"Command error: {error}")
                else:
                    printf(f"Illegal command: {opc}")
    
    def input(self, text):
        """Input text to the console."""
        if text:
            printf(f"] {text}")
            self.input_text = ""
            self.klp        = None
            self.hold_timer = 0
            try:
                self._proccmd(text)
            except Exception as error:
                printf(f"Error processing command '{text}': {error}")
                raise error