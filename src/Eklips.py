## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, gc, time, os
import requests
from classes.singleton import *
from classes.conhost import printf
from classes.constants_ekl import *

## No initialization code is here. Look at classes/singleton.py

## Run the engine
last_dt = time.time()
while (im_running):
    events = []
    try:
        # calculate delta time
        current_dt = time.time()
        delta = current_dt - last_dt # <- Delta time variable (0.1....)
        last_dt = current_dt

        # fill the interface if allowed
        if cvars.get("can_fill_screen?"):
            # empty screen if allowed to
            interface.fill(delta)

        # get events
        display.dispatch_events()
        events              = event.get_and_handle()
        mpos, mpressed      = event.get_mouse()
        keys_nheld          = event.key_once_map
        keys_pressed_dict   = event.key_map
        keys_pressed        = []

        # add key presses from dictionary to a list that only shows currently pressed keys
        for i in keys_pressed_dict:
            if keys_pressed_dict[i]:
                keys_pressed.append(i)
        
        # handle scene and signal                                                        
        try:
            scene.update(signal_sys, delta)
        except (BaseException, Exception) as error:
            ErrorHandler.error  = error     
            ErrorHandler.reason = scene.file_path
            events.append(PREMATURE_DEATH)  
        
        # handle events (most of them)                                                    
        if SOFT_QUIT in events:
            suicide()
            savefile.save_data()
            break
        
        # handle console                                                                  
        if is_key_pressed("eng_cheats"):
            console.toggle()

        # flip the screen
        clock.tick()
        if savefile.get("display/showfps", True):
            fps_display.draw()
        console.update(keys_nheld, keys_pressed, globals())
        interface.flip()
        event.key_once_map = []
    except (BaseException, Exception) as error:
        ErrorHandler.error  = error
        ErrorHandler.reason = "death_from_engine"
        events.append(PREMATURE_DEATH)
    
    # handle crashes
    if PREMATURE_DEATH in events:
        suicide()
        ErrorHandler.raise_error(ErrorHandler.error, ErrorHandler.reason, "bad coding skillz")
        break