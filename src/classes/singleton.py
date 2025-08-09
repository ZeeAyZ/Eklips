## Import all the libraries
import pyglet as pg
import Data, gc
from classes import UI, Save, Event, Signals, Nodes, Resources, CV, conhost
from classes.conhost import printf
from classes.key_entries import key_entries
from classes.constants_ekl import *
from typing import Any

## Print engine info
printf(f"{ENGINE_NAME} v{VER} ({BUILD_DATE})")

## Global states
events         = []
mpos, mpressed = [0,0], [0,0,0]

## Global variables
delta           : int                   = 0    
keys_pressed, keys_nheld                = [None],[None]
savefile        : Save.Savefile         = 0    
signal_sys      : Signals.SignalHandler = 0    
resource_loader : Resources.Loader      = 0    
display         : Any                   = 0    
batch           : pg.graphics.Batch     = 0    
icon            : pg.image.BufferImage  = 0    
global_stream   : pg.media.Player       = 0    
interface       : UI.Interface          = 0    
initialized     : bool                  = False
event           : Event.Event           = 0    
im_running      : bool                  = True 
ticks           : int                   = 0    
clock           : pg.clock.Clock        = 0    
scene           : Nodes.Scene           = 0    
console         : conhost.ConHost       = 0    
cvars           : CV.CvarCollection     = 0    
fps_display     : pg.window.FPSDisplay  = 0    

## Global functions
def reload_engine(dir=None):
    global savefile,signal_sys,resource_loader,cvars,console,keys_pressed,keys_nheld,display,batch,icon,initialized,interface,event,im_running,ticks,clock,scene, global_stream, fps_display
    """Reload/Load the engine variables."""
    
    ## Reload data and load cvars and print basic information
    gc.enable()
    cvars = Data._init()
    printf(f"{Data.game_name} v{Data.game_bdata['project-ver']} for {ENGINE_NAME} v{VER}")
    printf(" ~ Initializing CVARs")
    if dir:
        Data.data_directory = dir
        cvars.set("directory", dir, dir, "directoryParameterModifiedByArgument")

    ## Load libraries
    printf(" ~ Initializing savefile")
    savefile        = Save.Savefile()
    printf(" ~ Initializing signals")
    signal_sys      = Signals.SignalHandler()
    printf(" ~ Initializing ResourceMan")
    resource_loader = Resources.Loader()

    ## .. and then display
    if not initialized:
        printf(" ~ Initializing display")
        display   = pg.window.Window(
            savefile.get("display/resolution")[0], savefile.get("display/resolution")[1],
            caption    = Data.game_name,
            fullscreen = savefile.get("display/fullscreen"),
            vsync      = savefile.get("display/vsync"),
            file_drops = cvars.get("file_drops"),
            resizable  = True
        )
        fps_display = pg.window.FPSDisplay(display)
        batch       = pg.graphics.Batch()
        interface   = UI.Interface()
    else:
        interface.fill(0)
        interface.draw_queue.clear()
        interface.label_queue.clear()
        interface.sprite_used.clear()
        display.clear()
        display.set_size(savefile.get("display/resolution")[0], savefile.get("display/resolution")[1])
        display.set_caption(Data.game_name)
    icon      = pg.image.load(f"{Data.data_directory}/media/icon.png")
    display.set_icon(icon)
    

    ## .. more libraries
    printf(" ~ Initializing events")
    event         = Event.Event()
    clock         = pg.clock.Clock()
    console       = conhost.ConHost()
    global_stream = pg.media.Player()

    ## Scene data
    printf(f" ~ Initializing loading scene")
    scene_file = cvars.get("loading-scene")
    scene      = Nodes.Scene(scene_file)
    scene.load()
    
    ## hacking
    Data.game_bdata["keys"]["eng_cheats"] = {
        "keys": ["`","~"],
        "holdable": False
    }

    ## Set flag to true
    initialized = True

def load_new_scene(file):
    global scene
    """Load a new scene from a file path."""

    printf(f" ~ Initializing scene {file}")
    scene.file_path = file
    printf(f" ~ Emptying scene {scene.file_path}")
    scene.empty()
    printf(f" ~ Loading scene {scene.file_path}")
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

## Load the engine
reload_engine()