## Import all the libraries
import pyglet as pg
import classes.Singleton as engine
from classes.Constants import *

## Event class
class Event:
    def __init__(self):
        self.screen       = engine.display
        self.key_map      = {}
        self.key_once_map = []
        self.events       = []
        self.screen.push_handlers(self)
        self.mouse_pos = (0, 0)
        self.mouse_buttons = [0, 0, 0]  # Left, Middle, Right

    def on_close(self):
        self.events.append(('quit', None))
    
    # Keyboard
    def on_key_press(self,symbol, modifiers):
        self.events.append(('keydown', symbol))
        if symbol == pg.window.key.ESCAPE:
            return pg.event.EVENT_HANDLED

    def on_key_release(self, symbol, modifiers):
        self.events.append(('keyup', symbol))
    
    # Savefile
    def on_saved(self, successfully):
        self.events.append(('save', successfully))
    
    # Mouse
    def on_mouse_motion(self, x, y, dx, dy):
        self.mouse_pos = (x, y)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.mouse_pos = (x, y)

    def on_mouse_press(self, x, y, button, modifiers):
        if button == 1: self.mouse_buttons[0] = 1
        if button == 2: self.mouse_buttons[1] = 1
        if button == 4: self.mouse_buttons[2] = 1

    def on_mouse_release(self, x, y, button, modifiers):
        if button == 1: self.mouse_buttons[0] = 0
        if button == 2: self.mouse_buttons[1] = 0
        if button == 4: self.mouse_buttons[2] = 0
    
    def get(self):
        # Return and clear the queue
        events_copy = self.events[:]
        self.events.clear()
        return events_copy

    def get_and_handle(self):
        ## Events:
        # 0 - quit. 1 - keydown. 2 - keyup.
        events = self.get()
        code = []
        for i in events:
            if i[0] == 'quit':
                code.append(SOFT_QUIT)
            elif i[0] == 'keydown':
                code.append(KEYDOWN)
                self.key_map[i[1]] = 1
                self.key_once_map.append(i[1])
            elif i[0] == 'keyup':
                code.append(KEYUP)
                try:
                    self.key_map.pop(i[1])
                except:
                    self.key_map[i[1]] = 0
            elif i[0] == 'save':
                code.append(SAVE_EVENT)
                if i[1]:
                    code.append(SAVE_SUCESS)
                else:
                    code.append(SAVE_FAILED)
        return code

    def get_mouse(self):
        return [self.mouse_pos[0],self.screen.get_size()[1]-self.mouse_pos[1]], list(self.mouse_buttons)