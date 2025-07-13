## Import all the libraries
import pyglet as pg

## Event class
class Event:
    def __init__(self, window):
        self.screen  = window
        self.key_map = {}
        self.events  = []
        window.push_handlers(self)
        self.mouse_pos = (0, 0)
        self.mouse_buttons = [0, 0, 0]  # Left, Middle, Right

    # Simulate event queue
    def on_close(self):
        self.events.append(('quit', None))
    
    def on_key_press(self, symbol, modifiers):
        self.events.append(('keydown', symbol))

    def on_key_release(self, symbol, modifiers):
        self.events.append(('keyup', symbol))
    
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
    
    # Get that bitch
    def get(self):
        # Return and clear the queue like pygame.event.get()
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
                code.append(0)
            elif i[0] == 'keydown':
                code.append(1)
                self.key_map[i[1]] = 1
            elif i[0] == 'keyup':
                code.append(2)
                try:
                    self.key_map.pop(i[1])
                except:
                    self.key_map[i[1]] = 0
        return code

    def get_mouse(self):
        return [self.mouse_pos[0],self.screen.get_size()[1]-self.mouse_pos[1]], list(self.mouse_buttons)