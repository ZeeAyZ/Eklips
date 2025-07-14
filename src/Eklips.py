## Import all the libraries
import pyglet as pg
import ErrorHandler, json, Data, gc
from classes import UI, Save, Event, Signals, Nodes, Resources

## Print basic information and load version
print("### Eklips 4.0A")
ver = "4.0A"
ErrorHandler.ver = ver

## Ouch
savefile,signal_sys,resource_loader,display,batch,icon,interface,initialized,event,im_running,ticks,clock,scene_file,scene = 0,0,0,0,0,0,0,0,0,0,0,0,0,0
def reload_engine(dir=0, name=0):
    global savefile,signal_sys,resource_loader,display,batch,icon,initialized,interface,event,im_running,ticks,clock,scene_file,scene
    
    if not dir: dir = Data.data_directory
    if not name: name = Data.game_name

    Data.mod_data(dir,name)

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

## Actually load the engine
reload_engine()

def load_new_scene(file):
    global scene_file, scene
    print(f" ~ Initializing scene {scene_file}")
    scene_file  = file
    print(f" ~ Emptying scene {scene.file}")
    scene.file  = file
    scene.nodes = {}  
    print(f" ~ Loading scene {scene.file}")
    scene.load()      

## FPS Display
fps_display = pg.window.FPSDisplay(display)

## Ouch
def suicide():
    global im_running, interface, savefile, i_have_died
    interface.close()
    im_running  = 0
    i_have_died = 1
    savefile.save_data()

## .. and run it!
while (im_running):
    # empty screen
    try:
        #interface.fill()
        
        # get events
        display.dispatch_events()
        events              = event.get_and_handle()
        mpos, mpressed      = event.get_mouse()
        keys_pressed_barren = event.key_map
        keys_pressed        = []

        for i in keys_pressed_barren:
            if keys_pressed_barren[i]:
                keys_pressed.append(i)

        if ord('i') in keys_pressed:
            load_new_scene(Data.game_bdata["loading-scene"])
        
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
        if savefile.get("display/showfps"):
            fps_display.draw()
        interface.flip()
    except (BaseException, Exception) as e:
        suicide()
        ErrorHandler.raise_error(e, "from_scene", scene_file)
        break