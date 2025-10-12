## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, shutil, time, os
import classes.Singleton as engine
from classes.ConHost import printf
from classes.Constants import *

## No initialization code is here. Look at classes/engine.py

## Make Temp dir
os.makedirs("tmp", exist_ok=True)

## Run the engine
last_dt = time.time()
while (engine.im_running):
    engine.events = []
    try:
        # fill the interface if allowed
        if engine.cvars.get("can_fill_screen?"):
            try:
                # empty screen if allowed to
                engine.interface.fill(engine.delta)
            except Exception as error:
                ErrorHandler.error  = error
                ErrorHandler.reason = "UI (clearing screen)"
                engine.events.append(PREMATURE_DEATH)
        
        # calculate delta time
        engine.clock.get_delta() # Delta time variables
                                 #  engine.truedelta = can't be manipulated by game speed, good for ui
                                 #  engine.delta     = can

        # get events
        try:
            engine.display.dispatch_events()
            engine.events                   = engine.event.get_and_handle()
            engine.mpos, engine.mpressed    = engine.event.get_mouse()
            engine.keys_nheld               = engine.event.key_once_map
            engine.keys_pressed_dict        = engine.event.key_map
            engine.keys_pressed             = []
        except Exception as error:
            ErrorHandler.error  = error
            ErrorHandler.reason = "Reading User input"
            engine.events.append(PREMATURE_DEATH)

        # add key presses from dictionary to a list that only shows currently pressed keys
        try:
            for i in engine.keys_pressed_dict:
                if engine.keys_pressed_dict[i]:
                    engine.keys_pressed.append(i)
        except Exception as error:
            ErrorHandler.error  = error
            ErrorHandler.reason = "Key parsing"
            engine.events.append(PREMATURE_DEATH)
        
        # handle scene                                                        
        try:
            engine.scene.update(engine.delta)
        except (BaseException, Exception) as error:
            ErrorHandler.error  = error     
            ErrorHandler.reason = f"Scene {engine.scene.file_path}"
            engine.events.append(PREMATURE_DEATH)  
        
        # handle events (most of them)                                                    
        if SOFT_QUIT in engine.events:
            engine.suicide()
            engine.savefile.save_data()
            break
        
        # handle console                                                                  
        if engine.is_key_pressed("eng_cheats"):
            engine.console.toggle()

        # flip the screen
        try:
            if engine.savefile.get("display/showfps", True):
                engine.fps_display.draw()
            engine.console.update(engine.keys_nheld, engine.keys_pressed, globals())
            engine.interface.flip()
        except Exception as error:
            ErrorHandler.error  = error
            ErrorHandler.reason = "UI (updating window)"
            engine.events.append(PREMATURE_DEATH)

        engine.event.key_once_map = []
    except Exception as error:
        ErrorHandler.error  = error
        ErrorHandler.reason = "Engine, probably"
        engine.events.append(PREMATURE_DEATH)
    
    # handle crashes
    if PREMATURE_DEATH in engine.events:
        engine.suicide()
        ErrorHandler.raise_error(ErrorHandler.error, ErrorHandler.reason, "bad coding skillz")
        break

## Temp folder removal
shutil.rmtree("tmp", ignore_errors = True)
if "tmp" in os.listdir():
    shutil.rmtree("tmp", ignore_errors = True)
engine.scene.empty()