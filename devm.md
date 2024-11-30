## ![Eklips](img/icon.png) Developer Manual
This manual is for developers looking to use Eklips, if you are a user please go to the <a href=userm.md>User Manual</a>.

## Table of Contents
 1. [Setting up the data directory](#setting-up-the-data-directory)
 2. [Modifying basic assets](#modifying-basic-assets)
 3. [Documentation](#documentation)

## Setting up the data directory
In this repo of Eklips, the data directory is "eklips" which includes media, data, etc.. to modify the name, first rename the folder, and go to the `game.txt` file at the root which should look like:

```
Eklips 3.1.0
eklips
```

The first line is the name of the game which will be shown in the titlebar and the name of the user data directory (`~/Za9118/Eklips Engine`).
The second line is the name of the data folder (`eklips`), if you rename the data folder you need to change this line to the new name.

## Modifying basic assets
Now that you have your data folder set up, you can go to the `media` folder inside. Inside is:

```
icon.png      // Picture of your game icon
null.png      // Unused image
load.mp3      // Sound that plays when the game is loading
click.mp3     // Unused click noise
gdev.png      // Picture of your logo
eklips        // Folder with Eklips icons
 | icon.png   // Eklips icon
 | ring.png   // Used for loading animation
 | eklips.png // Used for loading animation
sheet         // Folder for spritesheets images, data is in *../data/sheet*
 | player.png // Player spritesheet
```

In this folder you can modify any of these files to your liking.

## Documentation
The Eklips engine uses a superset (`.ekeng\superset.sol`) config that contains all of the libraries. It is recommend to use the superset as the naming scheme in the code is a nightmare. (Will be fixed soon)

 - ### Eklips 
   This is a namespace that contains all libraries on the Eklips engine.

    - #### Eklips.Console
        This is the class that contains code that shows the console, the console can only be invoked by a script. The `eklips` folder has code that invokes the console by pressing the `key_cheats` key (defaulted to `).

        - #### Eklips.Console.Show()
            Make the console visible in the display.

        - #### Eklips.Console.Hide()
            Make the console invisible in the display.

        - #### Eklips.Console.printf(`text`)
            Add text to the console interface. Automatically ends with `\n`.

            ```
            text = A string that is the text to be displayed.
            ```
    
    - #### Eklips.Resource
        This is the class that loads every resource in the data folder on engine startup (images, audio, zipfiles, JSON files, etc..)
        Most functions here will save their outcome to memory to make it faster to remake them again. Remaking the same object is usually not a good idea. But so am i. 

        - #### Eklips.Resource.RenderText(`text, size, font, color`)
            Render text as a Surface. It also includes newline support.

            ```
            text = A string that is the text to be displayed. (REQUIRED)
            size = The size of the rendered text. (Optional, Default = 40)
            font = The font of the rendered text. (Optional, Default = Depends on config)
            color = the RGB color of the rendered text. (Optional, Default = (255, 255,255))
            ```

        - #### Eklips.Resource.Spritesheet(`name`)
            Returns a list of filenames of the spritesheet `name` that are in the `data/sheet` folder and `media/sheet` folder.

            ```
            name = The name of the spritesheet.
            ```
        
        - #### Eklips.Resource.get_font(`font, size`)
            Used by `Eklips.Resource.RenderText`. There is no point to use this function.

            It returns a font object of the font `font` and of size `size`.

            ```
            font = A string or None bool that is the font of the returned font object (REQUIRED)
            size = The size of the font object. (REQUIRED)
            ```
        
        - #### Eklips.Resource.Load(`asset`)
            Load the provided filename into memory for later use.

            ```
            asset = A string that is the filename of the asset. (REQUIRED)
            ```
    
    - ### Eklips.Networking
        This class implements a basic LAN socket networking system. It will be documented when complete.
    
    - ### Eklips.ReadProp(`file`)
        Read the custom INI-like file format (`.sol`) and return it as JSON.
        This might be confusing as the script file format is also `.sol`. Most `.sol` config files will start/have a line that starts with an `@`.
    
    - ### Eklips.Data
        A dictionary that contains important data such as the current language `["Lang"]`, Engine properties `["Engine"]`, etc.
    
    - ### Eklips.Player.Properties
        A `.sol` config file of player settings, located in `/data/instances/player.sol`. This file is not needed (Just like me) to run Eklips. But it's pretty nice to have a custom variable for.
    
    - ### Eklips.Save
        This is the class that handles your save file. The savefile is located in `%userprofile%/Eklips Engine/<Name of your game>`.

        - #### Eklips.Save.Get(`key, default`)
            Returns the value of the `key` path. If key path is not found, It returns `default` instead.

            ```
            key = A string that is path to the key (example: "path/to/key"), The keypath is translated into (example: Savefile["path"]["to"]["key"]) (REQUIRED)
            default = An object (string, integer, float, boolean, etc..) that is turned into the output if the key is not found. (Optional, Default = 0)
            ```
        
        - #### Eklips.Save.Set(`val, out`)
            Set a key path (`val`) into `out`.

            ```
            val = The key path to be modified (REQUIRED)
            out = An object (string, integer, float, boolean, etc..) that modifies the keypaths (val) value. Confusing i know. (REQUIRED)
            ```

        - #### Eklips.Save.Reset()
            Reset the savefile back to original settings (`/default_save.json`)
    
    - ### Eklips.UI
        This is the class that controls every draw call that makes this game engine a game engine. There is a whole bunch of functions. 

        - #### Eklips.UI.input(size, pos, AlwaysOn...)
            Displays an inputbox that allows the user to write on it
            Returns the value of the inputbox.
            
            ```
            size = The size of the inputbox (REQUIRED)
            pos = The position of the inputbox (REQUIRED)
            AlwaysOn = If the inputbox is always on
            anchor = The postion anchor of the inputbox
            scale = The size multiplier of the inputbox
            color = The color of the inputbox
            alpha = The opacity (0-1) of the inputbox
            special_flags = The special rendering flags, See pygame wiki for more info.
            cache = If the inputbox surface should be cached
            rotation = Rotation angle of the inputbox (Integer)
            disp = Surface to display this input
            clip = A portion of the inputbox to draw.
            flip = If the inputbox should be flipped
            placeholder = The text that is displayed if nothing has been written yet
            id = The ID of the input
            value = The value of the input
            event = A list of currently queued events
            frys = If the position cannot be changed by the parent being a frame
            ```

 - ### Sol 
   This is the same namespace as the Eklips namespace, but for backwards-compatibility as the Eklips engine used to be called Sol. We changed the name for people to not be confused to which Sol is our engine.