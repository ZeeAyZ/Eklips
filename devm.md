## ![Eklips](img/icon.png) Developer Manual
This manual is for developers looking to use Eklips, if you are a user please go to the <a href=userm.md>User Manual</a>.

## Table of Contents
 1. [Setting up the data directory](#setting-up-the-data-directory)
 2. [Modifying basic assets](#modifying-basic-assets)
 3. [Wiki](https://github.com/Za9-118/Eklips/wiki)

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

## Wiki
[Here](https://github.com/Za9-118/Eklips/wiki) is the wiki to the Sol superset language.