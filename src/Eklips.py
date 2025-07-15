## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, gc
from classes import UI, Save, Event, Signals, Nodes, Resources
from classes.key_entries import key_entries

## Print basic information and load version
print("### Eklips 4.0A")
ver = "4.0A"
ErrorHandler.ver = ver

## A mess
keys_pressed, keys_nheld = [],[]
savefile,signal_sys,resource_loader,display,batch,icon,interface,initialized,event,im_running,ticks,clock,scene_file,scene = 0,0,0,0,0,0,0,0,0,0,0,0,0,0

## Functions
def reload_engine(dir=0, name=0):
    global savefile,signal_sys,resource_loader,keys_pressed,keys_nheld,display,batch,icon,initialized,interface,event,im_running,ticks,clock,scene_file,scene
    """Reload/Load the engine variables."""

    ## Modify what project is being loaded if specified
    if not dir: dir = Data.data_directory
    if not name: name = Data.game_name

    Data.mod_data(dir,name)

    ## Empty this variable since.. uh.. yeah.
    keys_pressed = []
    keys_nheld   = []

    ## Load libraries
    print(" ~ Initializing savefile")
    savefile        = Save.Savefile(Data)
    print(" ~ Initializing signals")
    signal_sys      = Signals.SignalHandler()
    print(" ~ Initializing ResourceMan")
    resource_loader = Resources.Loader(Data)

    ## .. and then display
    print(" ~ Initializing display")
    if not initialized:
        display   = pg.window.Window(
            savefile.get("display/resolution")[0], savefile.get("display/resolution")[1],
            caption    = Data.game_name,
            fullscreen = savefile.get("display/fullscreen"),
            vsync      = savefile.get("display/vsync"),
            file_drops = Data.game_bdata["file_drops"],
            resizable  = True
        )
        batch = pg.graphics.Batch()
        icon = pg.image.load(f"{Data.data_directory}/media/icon.png")
        display.set_icon(icon)
        interface = UI.Interface(display, batch)
    else:
        display.set_size(savefile.get("display/resolution")[0], savefile.get("display/resolution")[1])
        display.set_caption(Data.game_name)
        icon = pg.image.load(f"{Data.data_directory}/media/icon.png")
        display.set_icon(icon)
        interface = UI.Interface(display, batch)

    initialized = 1

    ## .. more libraries
    print(" ~ Initializing events")
    event           = Event.Event(display)

    ## .. and make a bunch of variables!
    print(" ~ Adding values")
    im_running = 1
    ticks      = 0
    clock      = pg.clock.Clock()

    ## Scene data
    scene_file = Data.game_bdata["loading-scene"]
    print(f" ~ Initializing loading scene {scene_file}")
    scene      = Nodes.Scene(scene_file, interface, resource_loader, Data=Data)

def load_new_scene(file):
    global scene_file, scene
    """Load a new scene from a file path."""
    print(f" ~ Initializing scene {scene_file}")
    scene_file  = file
    print(f" ~ Emptying scene {scene.file}")
    scene.file  = file
    scene.nodes = {}  
    print(f" ~ Loading scene {scene.file}")
    scene.load()  
   
def suicide():
    global im_running, interface, savefile, i_have_died
    """Put the engine out of its misery"""
    interface.close()
    im_running  = 0
    i_have_died = 1
    savefile.save_data()

def is_key_pressed(key_name):
    """Get if a key is pressed from it's name. (Name; eg. 'moveup', 'movedown', etc...)"""
    global keys_pressed, keys_nheld
    for i in Data.game_bdata["keys"]:
        if i == key_name:
            key_data = Data.game_bdata["keys"][i]
            for key in key_data["keys"]:
                keyd = key_entries[key.upper()]
                if keyd in keys_pressed and key_data["holdable"]:
                    return 1
                if keyd in keys_nheld and not key_data["holdable"]:
                    return 1
    return 0

## Actually load the engine
reload_engine() 

## FPS Display
fps_display = pg.window.FPSDisplay(display)

## .. and run it!
while (im_running):
    try:
        if Data.game_bdata["can_fill_screen?"]:
            # empty screen if allowed to
            interface.fill()
        
        # get events
        display.dispatch_events()
        events              = event.get_and_handle()
        mpos, mpressed      = event.get_mouse()
        keys_nheld          = event.key_once_map
        keys_pressed_barren = event.key_map
        keys_pressed        = []

        # add key presses from dictionary to a list that only shows currently pressed keys
        for i in keys_pressed_barren:
            if keys_pressed_barren[i]:
                keys_pressed.append(i)
        
        # handle scene and signals      
        try:
            scene.update(Signals, globals())
        except (BaseException, Exception) as e:
            ErrorHandler.raise_error(e, "from_scene", scene_file)
            events.append(0)
        
        # handle events
        if 0 in events:
            suicide()
            break

        # flip the screen
        clock.tick()
        if savefile.get("display/showfps", 1):
            fps_display.draw()
        interface.flip()
        event.key_once_map = []
    except (BaseException, Exception) as e:
        suicide()
        ErrorHandler.raise_error(e, "from_scene", scene_file)
        break