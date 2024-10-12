## ![Sol](img/icon.png) Developer Manual
This manual is for developers looking to use Sol, if you are a user please go to the <a href=userm.md>User Manual</a>.

## Table of Contents
 1. [Setting up the data directory](#setting-up-the-data-directory)
 2. [Modifying basic assets](#modifying-basic-assets)

## Setting up the data directory
In this repo of Sol, the data directory is "sol" which includes media, data, etc.. to modify the name, first rename the folder (ofc), and go to the `game.txt` file at the root which should look like:

```
Sol Engine
sol
```

The first line is the name of the game which will be shown in the titlebar and the name of the user data directory (`~/Za9118/Sol Engine`).
The second line is the name of the data folder (`sol`), if you rename the data folder you need to change this line to the new name.

## Modifying basic assets
Now that you have your data folder set up, you can go to the `media` folder inside. Inside is:

```
icon.png     // Picture of your game icon
logo.png     // Picture of your game logo
null.png     // Null.png
load.mp3     // Sound that plays when loading
click.mp3    // Sound that plays when clicking
gdev.png     // Picture of your logo
sol          // Folder with Sol icons
 | icon.png  // Sol icon
 | ring.png  // Used for animation
 | sol.png   // Used for animation
sheet        // Folder for spritesheets images, data is in *../data/sheet*
 | player.png // Player spritesheet
```

In this folder you can modify any of these files to your liking.
