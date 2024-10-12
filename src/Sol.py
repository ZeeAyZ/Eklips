## Import
import pygame as pg
import tkinter
import traceback, socket, threading
import solhl
import time
import classes.overlay as overlay
from tkinter.messagebox import *
import os, time, json, threading, random, requests
from classes import res, fs, ui, sfxsys, kink, soleng, network as net
from classes.overlay import console, achievement, _overlay
import copy

## Init
pg.init()

## Display
display_size = pg.display.list_modes()[0]
flags = pg.FULLSCREEN
display=0
def setdisp(isSplash=0,SpSc="full"):
	global display, display_size, flags
	if isSplash:
		if SpSc=="":
			display = pg.display.set_mode((450,300), pg.NOFRAME)
		else:
			try:
				display = pg.display.set_mode(SpSc.get_size(), pg.NOFRAME)
			except:
				display = pg.display.set_mode((450,300), pg.NOFRAME)
	else:
		if SpSc=="full":
			display = pg.display.set_mode(display_size, flags)
		else:
			display = pg.display.set_mode(SpSc, flags)

resfol=open("game.txt").read().splitlines()[1]

## Caption
pg.display.set_caption(open("game.txt").read().splitlines()[0])

## Clock
clock = pg.time.Clock()

## Filesystem
fsm = fs.Filesystem(open("game.txt").read().splitlines())
setdisp(SpSc=fsm.val("Settings/display/res","full"))

## RescLoader
resld = res.ResourceLoader(resfol)

## Icon
try:
	pg.display.set_icon(resld.load(f"{resld.resfol}/media/icon.png"))
except:
	pg.display.set_icon(resld.load(f"{resld.resfol}/media/sol/icon.png"))

## SoundSystem
sfx = sfxsys.SoundSystem()
sfx.dvol = fsm.val("Settings/volume/mastervolume")

## User Interface
ux = ui.Interface(display, sfx, resld.load(f"{resld.resfol}/media/click.mp3"), resld)

## KinkReader
kinkr = kink.KinkVid(ux, resld)

## Sol related
try:
	sol_ver = open(f"{resld.resfol}/ver.txt").read().splitlines()[1]
except:
	sol_ver = "unknown"
sol = soleng.Engine()
solengi = sol
solcons = console.Console(ux, resld)
solwid = f"{resld.resfol}/{resld.resfol}.wid"

## Variables
running = 1
ticks = 1
fticks = 0
latest_key = 0

## Delta Time
old_dt = time.time()
dt = time.time()

## Game Data
data = {
	"Engine": {
		"MainMenu": 1,
		"Scene": "main",
		
		"Transition": "",
		"TAlpha": 0,
		"TAF": 1,
		"TSpeed": 1,

		"bsod": {
			"stage": 0
		},
		
		"GameAnimSpeed": 1,
		"Player": {
			"Pos": [0,0],
			"Vel": [10,10],
			"Flp": 0,
			"SessionName": 0,
			"Inventory": []
		},
		"CVar": {},
		"Level": {
			"Objects": {}
		}
	},
	
	"Lang": {},
	"Debug": 1
}

def servref(ip="", debug=0):
	e=net.ServerList(ip)
	return e.out

pb_con=""
pbcb=0
pbcs=0.1
servers={}

## Loader
loadscr = 1
loadthread = None
loading = 0
ldt = 0
ldts = 1
loadskp = fsm.val("Settings/load/loadskip")
loadno = fsm.val("Settings/load/noload")

## InstancePlayer properties
try:
	playermod = sol.read(f"{resld.resfol}/data/instances/player.sol")["info"]
except:
	print("Sol playermod gone, game errors expected")

## Spritesheet
try:
	playersheet = resld.sheet(playermod["file"])
except:
	print("Sol playersheet gone, game errors expected")

## Menu assets
bg = resld.load(resld.resfol+"/media/bg.png")
bg = pg.transform.scale(bg, display.get_size())
bgr=1
logotxt = resld.render(fsm.gm[0])

try:
	ev="start"
	sol.run(f"{resld.resfol}/data/scripts/event/{ev}.sol", gl=globals(), lc=locals())
except:
	print("Event error")

## Game loop
while (running):
	sfx.dvol = fsm.val("Settings/volume/mastervolume")
	old_dt = dt
	dt = time.time()
	speed=0.1
	delta = (dt - old_dt) * speed
	
	try:
		data["Lang"] = json.loads(open(f"{resld.resfol}/lang/{fsm.val('Settings/region/language')}.json").read())["content"]
	except:
		pass
	event = pg.event.get()
	event_key = pg.key.get_pressed()

	if soleng.Running != "":
		filesolmesg = f" (Running ({soleng.Running}))"
	
	try:
		# Handle events & keypresses/holds
		latest = 0
		for i in event:
			try:
				ev="pg_event"
				sol.run(f"{resld.resfol}/data/scripts/event/{ev}.sol", gl=globals(), lc=locals())
			except:
				print("Event error")
			if i.type == pg.QUIT:
				running = 0
				print("quit")
				try:
					ev="gm_close"
					sol.run(f"{resld.resfol}/data/scripts/event/{ev}.sol", gl=globals(), lc=locals())
				except:
					print("Event error")
			elif i.type == pg.KEYDOWN:
				try:
					ev="k_keydown"
					sol.run(f"{resld.resfol}/data/scripts/event/{ev}.sol", gl=globals(), lc=locals())
				except:
					print("Event error")
				for k in fsm.val("Settings/keys"):
					if fsm.val(f"Settings/keys/{k}") == pg.key.name(i.key):
						try:
							sol.run(f"{resld.resfol}/data/scripts/key/{k}.sol", gl=globals(),lc=locals())
						except:
							print("Key errors")
				try:
					latest_key = pg.key.name(i.key)
				except:
					pass
			elif i.type == pg.KEYUP:
				try:
					ev="k_keyup"
					sol.run(f"{resld.resfol}/data/scripts/event/{ev}.sol", gl=globals(), lc=locals())
				except:
					print("Event error")
			latest=pg.event.event_name(i.type)
		
		for k in fsm.val("Settings/keys"):
			ke = fsm.val(f"Settings/keys/{k}")
			if event_key[pg.key.key_code(ke)]:
				try:
					sol.run(f"{resld.resfol}/data/scripts/key/{k}.sol", gl=globals(),lc=locals())
				except:
					print("Key errors")
				try:
					latest_key = pg.key.name(i.key)
				except:
					pass
		
		# Loading
		if loadscr == 1:
			if fsm.val("Settings/load/splash") != "":
				setdisp(1,SpSc=resld.load(f"{resld.resfol}/{fsm.val('Settings/load/splash')}.png"))
				loadscr=0.9
				if not loading and not (loadno or loadskp):
					sfx.play(resld.load(f"{resld.resfol}/media/load.mp3"),cc="load.mp3", volume=0.2)
					try:
						playersheet = resld.sheet(playermod["file"])
					except:
						print("Game errors load player")
					loadthread = threading.Thread(target=resld.load_all, name="LoadingScreen-Resource-Loader")
					print("game: Loading Resources...")
					loadthread.run()
					loading = 1
				
				if loadno or loadskp:
					sfx.play(resld.load(f"{resld.resfol}/media/load.mp3"),cc="load.mp3", volume=0.2)
					loadscr=0.9
					loading=0
					ldt = 1
				
				if resld.ldone:
					if ldt < fsm.val("Settings/load/lddelay"):
						ldt += delta
					else:
						loadscr = 0.5
						loading = 0
						ldt = 1
						print("game: Loading Complete!")
			else:
				ux.blit(resld.load(f"{resld.resfol}/media/sol/sol.png"), [0,0], scale=2, anchor="cx cy")
				ux.blit(resld.load(f"{resld.resfol}/media/sol/ring.png"), [150,150], scale=2, anchor="cx cy",rotation=fticks*100)
				try:
					if fsm.val("Settings/load/showtips"):
						ux.blit(resld.render(data["Lang"]["tip1"]), [0,190], scale=0.75, anchor="cx cy")
					else:
						ux.blit(resld.render(data["Lang"]["load"]), [0,170], anchor="cx cy")
				except:
					pass	
				if not loading and not (loadno or loadskp):
					sfx.play(resld.load(f"{resld.resfol}/media/load.mp3"),cc="load.mp3")
					try:
						playersheet = resld.sheet(playermod["file"])
					except:
						print("Game errors load player")
					loadthread = threading.Thread(target=resld.load_all, name="LoadingScreen-Resource-Loader")
					print("game: Loading Resources...")
					loadthread.run()
					loading = 1
				
				if loadno or loadskp:
					sfx.play(resld.load(f"{resld.resfol}/media/load.mp3"),cc="load.mp3")
					loadscr=0.5
					loading=0
					ldt = 1

				if resld.ldone:
					if ldt < fsm.val("Settings/load/lddelay"):
						ldt += delta
					else:
						loadscr = 0.5
						loading = 0
						ldt = 1
						print("game: Loading Complete!")
		elif loadscr == 0.9:
			ux.blit(resld.load(f"{resld.resfol}/{fsm.val('Settings/load/splash')}.png"), [0,0])
			ldt -= delta * 2
			if ldt < 0.1:
				loadscr = 0
				ldt = 0
				ldts = 1
				loadskp=1
				setdisp(0)
		elif loadscr == 0.5: #LoadingFadeOut
			ux.blit(resld.load(f"{resld.resfol}/media/sol/sol.png"), [0,0], scale=2, anchor="cx cy", alpha=ldt)
			ux.blit(resld.load(f"{resld.resfol}/media/sol/ring.png"), [0,0], rotation=fticks*100, scale=2, anchor="cx cy", alpha=ldt)
			try:
				if fsm.val("Settings/load/showtips"):
					ux.blit(resld.render(data["Lang"]["tip1"]), [0,190], scale=0.75, anchor="cx cy")
				else:
					ux.blit(resld.render(data["Lang"]["load"]), [0,170], anchor="cx cy")
			except:
				pass	
			ldt -= delta * 2
			if ldt < 0.1:
				if not loadskp:
					loadscr = 0.25
				else:
					loadscr = 0
				ldt = 0
				ldts = 1
				loadskp=1
		elif loadscr == 0.25:
			#Developer credit
			ldt += delta * 2 * ldts
			if ldt > 1 and ldts == 1:
				ldts = -1
			elif ldt < 0 and ldts == -1:
				loadscr = 0
				ldt = 0
				ldts = 1
			
			ux.blit(resld.load(f"{resld.resfol}/media/gdev.png"), [0,0], scale=2, anchor="cx cy", alpha=ldt)
		else: # Script-based menu
			if data["Engine"]["MainMenu"]:
				if "bg" in fsm.val("Settings/peformance"):
					if fsm.val("Settings/peformance/bg"):
						if fsm.val("Settings/peformance/prlx"):
							ux.blit(bg, [0,0], anchor="cx cy")
						else:
							if bgr:
								ux.blit(bg, [0,0], anchor="cx cy", bo=0)
								bgr=0
					
				#try:
				sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
				#except:
				#	ux.blit(resld.load(f"{resld.resfol}/media/icon.png"), [50,50], size=(150,150))
				#	ux.blit(resld.render(data["Lang"]["munk"]), [250,100], scale=2, alpha=2)
				#	
				#	ux.blit(resld.render(data["Lang"]["munk1"]), [50,250], alpha=2)
			ticks += delta
		
		cmdpop = []
		for i in solcons.cmd:
			txtd=solcons.cmd[i]
			try:
				sol.run(f"{resld.resfol}/data/scripts/cmd/{txtd[0]}.sol", gl=globals(),lc=locals())
			except Exception as e:
				solcons.text += f"Error running script: {e}\n"
			showinfo("SolConsole", solcons.text)
			cmdpop.append(i)
		
		for i in cmdpop:
			solcons.cmd.pop(i)

		fps=clock.tick(fsm.val("Settings/peformance/fps"))
		solcons.draw(event)
		ux.render(fsm.val("Settings/display/FUNMODE"))
		ux.IncludeDebugOverlays = 1
		pg.display.flip()
		ux.tick()
		fticks += delta
	except Exception as error:
		running = 0
		fsm.save_dat()
		pg.quit()
		solhl.error(sol_ver+filesolmesg, error)

pg.quit()
fsm.close()
fsm.save_dat()