## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, gc, time
from classes import UI, Save, Event, Signals, Nodes, Resources, CV
from classes import conhost
from classes.conhost import printf
from classes.key_entries import key_entries
from classes.data_ekl import *

## Print basic information
printf(f"### Eklips {VER} / {Data.game_name} {Data.game_bdata['project-ver']}")

## Basic garbage collection
gc.enable()

## A mess
keys_pressed, keys_nheld = [],[]               
savefile        : Save.Savefile         = 0    
signal_sys      : Signals.SignalHandler = 0    
resource_loader : Resources.Loader      = 0    
display         : Unknown               = 0 # Pylance is being a bitch, and, to be honest,
                                            # why use this variable when the interface variable exists?
batch           : pg.graphics.Batch     = 0    
icon            : pg.image.BufferImage  = 0    
interface       : UI.Interface          = 0    
initialized     : bool                  = False
event           : Event.Event           = 0    
im_running      : bool                  = True 
ticks           : int                   = 0    
clock           : pg.clock.Clock        = 0    
scene_file      : str                   = ""   
scene           : Nodes.Scene           = 0    
console         : conhost.ConHost       = 0    
cvars           : CV.CvarCollection     = 0    

## Functions
def reload_engine(dir=0, name=0):
    global savefile,signal_sys,resource_loader,cvars,console,keys_pressed,keys_nheld,display,batch,icon,initialized,interface,event,im_running,ticks,clock,scene_file,scene
    """Reload/Load the engine variables."""

    ## Modify what project is being loaded if specified
    if not dir: dir = Data.data_directory
    if not name: name = Data.game_name

    Data.mod_data(dir,name)

    ## Empty this variable since.. uh.. yes.
    keys_pressed = []
    keys_nheld   = []

    ## Load libraries
    printf(" ~ Initializing savefile")
    savefile        = Save.Savefile(Data)
    printf(" ~ Initializing signals")
    signal_sys      = Signals.SignalHandler()
    printf(" ~ Initializing ResourceMan")
    resource_loader = Resources.Loader(Data, savefile)

    ## .. and then display
    if not initialized:
        printf(" ~ Initializing display")
        display   = pg.window.Window(
            savefile.get("display/resolution")[0], savefile.get("display/resolution")[1],
            caption    = Data.game_name,
            fullscreen = savefile.get("display/fullscreen"),
            vsync      = savefile.get("display/vsync"),
            file_drops = Data.game_bdata["file_drops"],
            resizable  = True
        )
        batch    = pg.graphics.Batch()
        icon     = pg.image.load(f"{Data.data_directory}/media/icon.png")
        display.set_icon(icon)
        interface = UI.Interface(display, batch)
    else:
        display.set_size(savefile.get("display/resolution")[0], savefile.get("display/resolution")[1])
        display.set_caption(Data.game_name)
        icon      = pg.image.load(f"{Data.data_directory}/media/icon.png")
        display.set_icon(icon)
        interface = UI.Interface(display, batch)

    ## .. more libraries
    printf(" ~ Initializing events")
    event   = Event.Event(display)
    clock   = pg.clock.Clock()
    cvars   = CV.CvarCollection()
    console = conhost.ConHost(interface, cvars)

    ## Scene data
    printf(f" ~ Initializing loading scene")
    scene_file = Data.game_bdata["loading-scene"]
    scene      = Nodes.Scene(scene_file, interface, resource_loader, Data=Data)
    
    ## Hacking!
    Data.game_bdata["keys"]["eng_cheats"] = {
        "keys": ["`","~"],
        "holdable": False
    }
    
    initialized = True

def load_new_scene(file):
    global scene_file, scene
    """Load a new scene from a file path."""
    printf(f" ~ Initializing scene {scene_file}")
    scene_file  = file
    printf(f" ~ Emptying scene {scene.file}")
    scene.file  = file
    scene.empty()
    printf(f" ~ Loading scene {scene.file}")
    scene.load()  
   
def suicide():
    global im_running, interface, savefile, i_have_died
    """Kill the engine"""
    interface.close()
    im_running  = 0
    i_have_died = 1
    savefile.save_data()

def is_key_pressed(key_name):
    """Get if a key is pressed from its name entry. (Name; eg. 'moveup', 'movedown', etc...)"""
    global keys_pressed, keys_nheld
    for i in Data.game_bdata["keys"]:
        if i == key_name:
            key_data = Data.game_bdata["keys"][i]
            for key in key_data["keys"]:
                keyd = key_entries[key.upper()]
                if keyd in keys_pressed and key_data["holdable"]:
                    return True
                if keyd in keys_nheld and not key_data["holdable"]:
                    return True
    return False

## Actually load the engine
reload_engine() 

## FPS Display
fps_display = pg.window.FPSDisplay(display)

## Delta time
last_dt = time.time()

## .. and run it!
while (im_running):
    events = []
    try:
        # calculate delta time
        current_dt = time.time()
        delta = current_dt - last_dt # <- Delta time variable (0.1....)
        last_dt = current_dt

        # fill the interface if allowed
        if Data.game_bdata["can_fill_screen?"]:
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
        
        # handle scene and signals      
        try:
            scene.update(Signals, globals())
        except (BaseException, Exception) as error:
            ErrorHandler.error  = error
            ErrorHandler.reason = scene_file
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
        if savefile.get("display/showfps", 1):
            fps_display.draw()
        console.update(keys_nheld, keys_pressed)
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