## Import all the libraries 
import pyglet as pg
import Data, gc
from classes            import UI, Save, Event, Resources, CV, Scene, ConHost, Clock, fpsdisp
from classes.ConHost    import printf
from classes.KeyEntries import key_entries
from classes.Constants  import *
from tkinter.messagebox import *
from typing import Any

## Print engine info
printf(f"{ENGINE_NAME} v{VER} ({BUILD_DATE})")

## Global states
events         = []
mpos, mpressed = [0,0], [0,0,0]

## Global variables
pacing          : int                   = 1             # delta = (calculate delta here) * pacing
old_pacing      : int                   = pacing        # Run it back
obj_ids         : int                   = 10            
delta           : int                   = 0             
truedelta       : int                   = 0             
keys_pressed, keys_nheld                = [None],[None] 
savefile        : Save.Savefile         = 0             
resource_loader : Resources.Loader      = 0             
display         : Any                   = 0             
batch           : pg.graphics.Batch     = 0             
icon            : pg.image.BufferImage  = 0             
global_stream   : pg.media.Player       = 0             
interface       : UI.Interface          = 0             
initialized     : bool                  = False         
event           : Event.Event           = 0             
im_running      : bool                  = True          
ignore_os       : bool                  = False
ticks           : int                   = 0             
clock           : Clock.Time            = 0             
scene           : Scene.Scene           = 0             
console         : ConHost.ConHost       = 0             
cvars           : CV.CvarCollection     = 0             
fps_display     : fpsdisp.FPSDisplay    = 0             
cam_pos         : list                  = [0,0,0]
cam_zoom        : int                   = 0
thm             : Resources.Theme       = 0

## Global functions
def reload_engine(dir=None):
    global savefile,resource_loader,cvars,console,thm,keys_pressed,keys_nheld,display,batch,icon,initialized,interface,event,im_running,ticks,clock,scene, global_stream, fps_display
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
        batch       = pg.graphics.Batch()
        interface   = UI.Interface()
    else:
        # Empty the screen
        interface.fill(0)

        # Remove all sprites
        interface.draw_queue.clear()
        interface.label_queue.clear()
        interface.sprite_used.clear()

        # Clear display and reset everything
        display.clear()
        display.set_size(savefile.get("display/resolution")[0], savefile.get("display/resolution")[1])
        display.set_caption(Data.game_name)
    
    icon_path = cvars.get("icon_file", "mem://unknown")
    icon      = resource_loader.load(icon_path).get()
    display.set_icon(icon)

    ## .. more libraries
    printf(" ~ Initializing events")
    event         = Event.Event()
    clock         = Clock.Time()
    console       = ConHost.ConHost()
    global_stream = pg.media.Player()
    fps_display   = fpsdisp.FPSDisplay(display)

    ## Theme
    thm_path = cvars.get("theme_file", "mem://unknown_theme")
    thm      = resource_loader.load(thm_path)

    ## Scene data
    printf(f" ~ Initializing loading scene")
    scene_file = cvars.get("loading-scene")
    scene      = Scene.Scene(scene_file)
    scene.load()
    
    ## Ouch
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
    try:
        interface.close()
    except:
        print("Error; the app could not be closed")
    im_running  = False
    i_have_died = True
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

def get_mouse_scroll():
    return event.mouse_scroll

## Load the engine
reload_engine()