## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, gc, time, os
import requests
import classes.singleton as singleton
from classes.conhost import printf
from classes.constants_ekl import *

## No initialization code is here. Look at classes/singleton.py

## Run the engine
last_dt = time.time()
while (singleton.im_running):
    events = []
    try:
        # calculate delta time
        current_dt = time.time()
        singleton.delta = current_dt - last_dt # <- Delta time variable (0.1....)
        last_dt = current_dt

        # fill the interface if allowed
        if singleton.cvars.get("can_fill_screen?"):
            # empty screen if allowed to
            singleton.interface.fill(singleton.delta)

        # get events
        singleton.display.dispatch_events()
        singleton.events                   = singleton.event.get_and_handle()
        singleton.mpos, singleton.mpressed = singleton.event.get_mouse()
        singleton.keys_nheld               = singleton.event.key_once_map
        singleton.keys_pressed_dict        = singleton.event.key_map
        singleton.keys_pressed             = []

        # add key presses from dictionary to a list that only shows currently pressed keys
        for i in singleton.keys_pressed_dict:
            if singleton.keys_pressed_dict[i]:
                singleton.keys_pressed.append(i)
        
        # handle scene                                                        
        try:
            singleton.scene.update(singleton.delta)
        except (BaseException, Exception) as error:
            ErrorHandler.error  = error     
            ErrorHandler.reason = singleton.scene.file_path
            singleton.events.append(PREMATURE_DEATH)  
        
        # handle events (most of them)                                                    
        if SOFT_QUIT in singleton.events:
            singleton.suicide()
            singleton.savefile.save_data()
            break
        
        # handle console                                                                  
        if singleton.is_key_pressed("eng_cheats"):
            singleton.console.toggle()

        # flip the screen
        singleton.clock.tick()
        if singleton.savefile.get("display/showfps", True):
            singleton.fps_display.draw()
        singleton.console.update(singleton.keys_nheld, singleton.keys_pressed, globals())
        singleton.interface.flip()
        singleton.event.key_once_map = []
    except (BaseException, Exception) as error:
        ErrorHandler.error  = error
        ErrorHandler.reason = "death_from_engine"
        singleton.events.append(PREMATURE_DEATH)
    
    # handle crashes
    if PREMATURE_DEATH in singleton.events:
        singleton.suicide()
        ErrorHandler.raise_error(ErrorHandler.error, ErrorHandler.reason, "bad coding skillz")
        break