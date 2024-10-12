import pygame as pg
import random
from collections import OrderedDict

class SurfaceCache:
	def __init__(self, max_size=10):
		self.cache = OrderedDict()
		self.max_size = max_size
		self.button_data = {}

	def cache_surface(self, key, surf):
		if len(self.cache) >= self.max_size:
			# Remove the least recently used item
			self.cache.popitem(last=False)
		self.cache[key] = surf

	def get_cached_surface(self, key):
		if key in self.cache:
			# Move to the end (most recently used)
			self.cache.move_to_end(key)
			return self.cache[key]
		return None

pg.font.init()
class Interface:
	def __init__(self, display, sfx, clk, res):
		self.display = display
		self.font = pg.font.Font(None, 35)
		self.sfx = sfx #SfxPlayer
		self.cache = SurfaceCache(max_size=10)
		self.button_data = {}
		self.layerold = {}
		self.ticks = 0
		self.clk = clk #ClickSound
		self.iscl = {} #IsClicking
		self.IncludeDebugOverlays = 1
		self.frames = {}
		self.res = res
		self.cmpm = 0 #CompatibleMobileButtons
		self.inputs = {}
		self.layers = {}
		self.sliders = {}
	
	def input(self, size, pos, AlwaysOn=0, anchor="", scale=1, alpha=1, special_flags=0, cache=False, rotation=0, disp="display", clip=0, flip=0, placeholder="", id=None, value="", event=None, frys=0):
		if event == None:
			event = pg.event.get()
		
		if disp == "display":
			disp = self.display
		
		if id == None:
			cache_key = f"InputObject-{size[0]}:{size[1]}:{scale}:{alpha}:{placeholder}:{rotation}:{size}:{flip}"
		else:
			cache_key = id
		
		if not cache_key in self.inputs:
			self.inputs[cache_key] = {
				"placeholder": placeholder,
				"value": value,
				"return": 0,
				"blink": 0,
				"selected": 0
			}
		
		# Blink
		blnk="_"
		if self.inputs[cache_key]["blink"]:
			blnk="_"
		else:
			blnk=" "
		if not self.inputs[cache_key]["selected"] or not AlwaysOn:
			blnk=" "
		self.inputs[cache_key]["blink"] = not self.inputs[cache_key]["blink"]
		
		# Render input
		if self.inputs[cache_key]["value"] != "":
			f=self.res.render(self.inputs[cache_key]["value"]+blnk, color="black")
			surf = pg.Surface((f.get_width(), f.get_height()*2), pg.SRCALPHA)
			surf.blit(f, [10,10])
			
			if not AlwaysOn:
				inp = self.button(surf, pos, anchor, scale, alpha, 0, special_flags, cache, 0.1, disp, 0, frys=frys)
			else:
				inp = self.blit(surf, pos, anchor=anchor, scale=scale, alpha=alpha, disp=disp)
		else:
			f=self.res.render(self.inputs[cache_key]["placeholder"]+blnk, color=(127,127,127))
			surf = pg.Surface((f.get_width(), f.get_height()))
			surf.fill((200, 200, 200))
			surf.blit(f, [10,10])
			
			if not AlwaysOn:
				inp = self.button(surf, pos, anchor, scale, alpha, 0, special_flags, cache, 0.1, disp, 0, frys=frys)
			else:
				inp = self.blit(surf, pos, anchor=anchor, scale=scale, alpha=alpha, disp=disp)
		
		# Input logic
		if inp:
			self.inputs[cache_key]["selected"] = not self.inputs[cache_key]["selected"]
		
		if self.inputs[cache_key]["selected"] or AlwaysOn:
			for i in event:
				if i.type == pg.KEYDOWN:
					if i.key == pg.K_RETURN:
						self.inputs[cache_key]["return"] = 1
					elif i.key == pg.K_BACKSPACE:
						self.inputs[cache_key]["value"] = self.inputs[cache_key]["value"][:-1]
					else:
						try:
							self.inputs[cache_key]["value"] += chr(i.key)
						except:
							try:
								self.inputs[cache_key]["value"] += pg.key.name(i.key)
							except:
								pass
		
		return self.inputs[cache_key]["value"]
	
	def frame(self, size, pos, anchor="", sxs=1, scale=1, alpha=1, special_flags=0, cache=False, rotation=0, disp="display", clip=0, flip=0, scrollable=1, id=None, frys=0):
		surf = pg.Surface(size)
		surf.fill((200, 200, 200))
		dispd={}
		
		if disp=="display":
			disp=self.display
		else:
			if type(disp).__name__ == "dict":
				dispd=disp
				if "AvailabilityCheckIsDisplay" in dispd:
					disp=dispd["surf"]
				if "AvailabilityCheckIsFrameObject" in dispd and not frys:
					pos[0]-=self.frames[dispd["AvailabilityCheckIsFrameObject"]]["x"]
					pos[1]-=self.frames[dispd["AvailabilityCheckIsFrameObject"]]["y"]
			elif type(disp).__name__ == "Surface":
				disp=disp
		
		# Create a unique cache key
		if id == None:
			cache_key = f"Frame-{size[0]}:{size[1]}:{scale}:{alpha}:{24}:{rotation}:{size}:{flip}"
		else:
			cache_key = id
		
		if not cache_key in self.frames:
			self.frames[cache_key] = {"x": 0, "y": 0, "totaly": 0}
		data=self.frames[cache_key]
		
		if flip != 0:
			surf = pg.transform.flip(surf, flip)
		if rotation != 0:
			surf = pg.transform.rotate(surf, rotation)
		if scale != 1:
			surf = pg.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
			if clip != 0:
				tmp=list(clip)
				clip=[
					tmp[0]*scale,
					tmp[1]*scale,
					tmp[2]*scale,
					tmp[3]*scale
				]
		if alpha != 1:
			surf.set_alpha(int(alpha * 255))

		# Adjust position based on anchor
		display_width = disp.get_width()
		display_height = disp.get_height()
		surf_width = surf.get_width()
		surf_height = surf.get_height()
		if clip:
			surf_width=clip[2]
			surf_height=clip[3]

		if "right" in anchor:
			pos[0] = display_width - pos[0] - surf_width
		if "bottom" in anchor:
			pos[1] = display_height - pos[1] - surf_height
		if "cx" in anchor:
			pos[0] += display_width / 2 - surf_width / 2
		if "cy" in anchor:
			pos[1] += display_height / 2 - surf_height / 2

		# Blit the surface onto the display
		if clip:
			sprite = disp.blit(surf, pos, clip, special_flags=special_flags)
		else:
			sprite = disp.blit(surf, pos, special_flags=special_flags)

		# Check for mouse interactions
		mrect = self.mrect()

		# Check if hovering and calculate distance safely
		hovering = sprite.colliderect(mrect)

		# Prevent division by zero in distance calculation
		x_dist = mrect.x - sprite.x + 0.0001
		y_dist = mrect.y - sprite.y + 0.0001

		distance = x_dist / y_dist
		click = pg.mouse.get_pressed()
		clicking_cmp = self.clicking(sprite, cache_key)
		if clip:
			sprite = self.blit(surf, pos, clip, special_flags=special_flags)
		else:
			sprite = self.blit(surf, pos, special_flags=special_flags)
		if scrollable:
			barbIsBig=((self.frames[cache_key]["y"]+1)/10)
			if barbIsBig < 1:
				barbIsBig=1
			barbIsBigd=barbIsBig
			if barbIsBigd/2 < 1:
				barbIsBigd=1
			dys=data["y"]
			if dys > size[1] - 80 - (barbIsBig):
				dys=size[1] - 80 - (barbIsBig)
			barb = self.button(self.res.load(f"{self.res.resfol}/media/ui/scroll_y.png"), [25,25+dys], anchor="right", size=(20, 40 - (barbIsBigd / 2)), scale=2-(sxs-1), disp=sprite)
			if barb:
				aftm = self.frames[cache_key]["y"] + ((pg.mouse.get_rel()[1] * (sxs /2)) + (barbIsBig/2))
				if aftm > 0 and aftm < size[1] - 80 - (barbIsBig):
					self.frames[cache_key]["y"] = aftm
					self.frames[cache_key]["totaly"] = aftm

		# Return relevant Frame() information
		dataframe = {
			"sprite": sprite,
			"click": {
				0: clicking_cmp and click[0],
				1: clicking_cmp and click[1],
				2: clicking_cmp and click[2],
				"*": 1 in click
			},
			"FrameObjData": self.frames[cache_key],
			"hovering": hovering,
			"distance": distance,
			"AvailabilityCheckIsDisplay": 1,
			"AvailabilityCheckIsFrameObject": cache_key,
			"surf": surf,
			"Pos": pos
		}
		return dataframe
	
	def clicking(self, obj, id=1):
		if not id in self.iscl:
			self.iscl[id] = 0
		if self.cmpm:
			for i in pg.event.get():
				if i.type == pg.MOUSEBUTTONDOWN:
					if obj.colliderect(self.mrect()):
						self.iscl[id] = 0
				elif i.type == pg.MOUSEBUTTONUP:
					if obj.colliderect(self.mrect()):
						self.iscl[id] = 1
		else:
			self.iscl[id] = obj.colliderect(self.mrect())
		return self.iscl[id]

	def rect(self, col, size):
		# Create a rectangle with a color
		surf = pg.Surface(size)
		surf.fill(col)
		return surf
	
	def tick(self):
		# Tick
		self.ticks += 1
	
	def fill(self, color, disp="display",alpha=1, off=[0,0],size="disp", anchor=""):
		if disp=="display":
			disp=self.display
		# Fill the screen
		if size=="disp":
			size=(disp.get_width(), disp.get_height())
		try:
			self.blit(self.rect(color, size), off, disp=disp, alpha=alpha, anchor=anchor)
		except:
			print("RectCol Err")
			
	# Function to create or reuse a button
	def button(self, surf, pos, id="", anchor="", size=0, scale=1, alpha=1, click=0, special_flags=0, cache=True, delta=0.1, oppo=0, disp="display", disabled=0, frys=0, cooldown=0.1):
		if disp=="display":
			disp=self.display
		# Create a unique cache key based on the button's characteristics
		if id == "":
			button_id = f"Button-{surf.get_width()}:{surf.get_height()}:{scale}:{alpha}:{20}"
		else:
			button_id = id
		
		if not button_id in self.button_data:
			# Create and store the button in the cache if it doesn't exist
			self.button_data[button_id] = [1, alpha, 0]
		
		data = self.button_data[button_id]
		
		# Add White Backdrop so the button doesn't turn pitch black
		surft = pg.Surface(surf.get_size())
		surft.fill((255,255,255))

		if size == 0:
			size = surf.get_size()

		# Draw the button and check if the button is being hovered
		if disabled:
			asset={"click": {}}
			asset_txtr = self.blit(surf, pos, anchor, scale, alpha/2, special_flags, disp=disp, clks=0, frys=frys, size=size)
			asset["click"][1]=0
			asset["click"][2]=0
			asset["click"][3]=0
			asset["click"][0]=0
			asset["hovering"]=0
		else:
			asset = self.blit(surft, pos, anchor, scale, 0, special_flags, disp=disp, clks=0, frys=frys, size=size)
			asset_txtr = self.blit(surf, pos, "", scale, alpha/data[0], special_flags, disp=disp, frys=frys, size=size)
		
		if type(delta).__name__ != "int":
			delta = 0.1
		if oppo:
			if asset["hovering"]:
				if data[0] > alpha:
					data[0] -= delta
			else:
				if data[0] < 2:
					data[0] += delta
		else:
			if asset["hovering"]:
				if data[0] < 2:
					data[0] += delta
			else:
				if data[0] > alpha:
					data[0] -= delta
		
		clicked=asset["click"][click]
		return clicked
	
	#mrect: Mouse rect
	def mrect(self, width=10, height=10):
		# Get the current mouse position
		mouse_pos = pg.mouse.get_pos()

		# Create a pg.Rect based on the mouse position and desired size
		mrect = pg.Rect(
			mouse_pos[0] - width // 2,  # Center the rect horizontally
			mouse_pos[1] - height // 2,  # Center the rect vertically
			width,					   # Width of the mouse rectangle
			height					   # Height of the mouse rectangle
		)

		return mrect
	
	def blit(self, surf, pos, anchor="", scale=1, alpha=1, special_flags=0, cache=False, rotation=0,size=1, disp="display", clip=0, flip=0, clks=1, frys=0, layer=0, id=0, bo=1):
		dispd={}
		if disp=="display":
			disp=self.display
		else:
			if type(disp).__name__ == "dict":
				dispd=disp
				if "AvailabilityCheckIsDisplay" in dispd:
					disp=dispd["surf"]
			elif type(disp).__name__ == "Surface":
				disp=disp
		if scale < 1:
			scale=1
		# Create a unique cache key
		try:
			cache_key = f"Surface-{surf.get_width()}:{surf.get_height()}:{scale}:{alpha}:{21}:{rotation}:{size}:{flip}"
		except:
			cache_key = f"Surface-Unknown-Unknown-{scale}-{alpha}-{rotation}-{size}-{flip}"
		
		if id == 0:
			id = len(self.layers)+1
		lk=f"{cache_key};{id}"
		if not lk in self.layers:
			self.layers[lk]={"data": {}}
		
		if cache:
			# Get from cache if available
			cached_surf = self.cache.get_cached_surface(cache_key)
			if cached_surf:
				surf = cached_surf
			else:
				# Apply transformations and cache it
				if size != 1:
					size=list(size)
					if size[0] < 1:
						size[0]=abs(size[0])
						pos[0]+=size[0]
					if size[1] < 1:
						size[1]=abs(size[1])
						pos[1]+=size[1]
					surf = pg.transform.scale(surf, size)
				if flip != 0:
					surf = pg.transform.flip(surf, flip)
				if rotation != 0:
					surf = pg.transform.rotate(surf, rotation)
				if scale != 1:
					surf = pg.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
					tmp=clip
					clip=[tmp[0]*scale, tmp[1]*scale, tmp[2]*scale, tmp[3]*scale]
				if alpha != 1:
					surf.set_alpha(int(alpha * 255))
				self.cache.cache_surface(cache_key, surf)
		else:
			# Apply transformations if not using cache
			if size != 1:
				size=list(size)
				if size[0] < 1:
					size[0]=abs(size[0])
					pos[0]-=size[0]
				if size[1] < 1:
					size[1]=abs(size[1])
					pos[1]-=size[1]
				surf = pg.transform.scale(surf, size)
			if flip != 0:
				surf = pg.transform.flip(surf, flip)
			if rotation != 0:
				surf = pg.transform.rotate(surf, rotation)
			if scale != 1:
				surf = pg.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
				if clip != 0:
					tmp=list(clip)
					clip=[
						tmp[0]*scale,
						tmp[1]*scale,
						tmp[2]*scale,
						tmp[3]*scale
					]
			if alpha != 1:
				surf.set_alpha(int(alpha * 255))

		# Default fallback surface if not valid
		if not surf:
			surf = pg.Surface((200, 200))
			surf.fill((255, 0, 0))

		# Adjust position based on anchor
		try:
			display_width = disp.get_width()
			display_height = disp.get_height()
		except:
			display_width = self.display.get_width()
			display_height = self.display.get_height()
		surf_width = surf.get_width()
		surf_height = surf.get_height()
		if clip:
			surf_width=clip[2]
			surf_height=clip[3]

		try:
			if "right" in anchor:
				pos[0] = display_width - pos[0] - surf_width
			if "bottom" in anchor:
				pos[1] = display_height - pos[1] - surf_height
			if "cx" in anchor:
				pos[0] += display_width / 2 - surf_width / 2
			if "cy" in anchor:
				pos[1] += display_height / 2 - surf_height / 2
		except:
			print("Anchors Broken")
		if "AvailabilityCheckIsFrameObject" in dispd and not frys:
			pos[0]-=self.frames[dispd["AvailabilityCheckIsFrameObject"]]["x"]
			pos[1]-=self.frames[dispd["AvailabilityCheckIsFrameObject"]]["y"]
		
		# Blit the surface onto the display
		"""
		try:
			if clip:
				sprite = disp.blit(surf, pos, clip, special_flags=special_flags)
			else:
				sprite = disp.blit(surf, pos, special_flags=special_flags)
		except:
			if clip:
				sprite = self.display.blit(surf, pos, clip, special_flags=special_flags)
			else:
				sprite = self.display.blit(surf, pos, special_flags=special_flags)
		"""

		sxo,syo=0,0
		if "AvailabilityCheckIsFrameObject" in dispd and not frys:
			sxo,syo=self.frames[dispd["AvailabilityCheckIsFrameObject"]]["x"], self.frames[dispd["AvailabilityCheckIsFrameObject"]]["y"]
		try:
			sprite=pg.rect.Rect((dispd["Pos"][0]+pos[0]-sxo, dispd["Pos"][1]+pos[1]-syo), (surf.get_width(), surf.get_height()))
		except:
			sprite=pg.rect.Rect((pos[0]-sxo, pos[1]-syo), (surf.get_width(), surf.get_height()))
		# Check for mouse interactions
		mrect = self.mrect()

		# Check if hovering and calculate distance safely
		hovering = sprite.colliderect(mrect)

		# Prevent division by zero in distance calculation
		x_dist = mrect.x - sprite.x + 0.0001
		y_dist = mrect.y - sprite.y + 0.0001

		distance = x_dist / y_dist
		click = pg.mouse.get_pressed()
		
		clicking_cmp = self.clicking(sprite, cache_key)
		
		if clicking_cmp and 1 in click and clks:
			pass#self.sfx.play(self.clk, cc="click.mp3")
		
		if "AvailabilityCheckIsDisplay" in dispd:
			self.blit(disp, dispd["Pos"])
		
		#Return Black Surface
		if bo:
			surfb=pg.Surface(surf.get_size())
			surfb.fill("black")
			self.layers[f"o{lk}"] = {
				"data": {
					"sprite": sprite,
					"click": {
						0: clicking_cmp and click[0],
						1: clicking_cmp and click[1],
						2: clicking_cmp and click[2],
						"*": 1 in click
					},
					"hovering": hovering,
					"distance": distance,
					"AvailabilityCheckIsDisplay": 1,
					"surf": surfb,
					"Pos": pos,
					"Layer": -1,
					"LayerID": f"o{lk}",
					"Clip": clip,
					"Disp": disp,
					"SpecialFlags": 0
				}
			}

		# Return relevant information
		data={
			"sprite": sprite,
			"click": {
				0: clicking_cmp and click[0],
				1: clicking_cmp and click[1],
				2: clicking_cmp and click[2],
				"*": 1 in click
			},
			"hovering": hovering,
			"distance": distance,
			"AvailabilityCheckIsDisplay": 1,
			"surf": surf,
			"Pos": pos,
			"Layer": layer,
			"LayerID": lk,
			"Clip": clip,
			"Disp": disp,
			"SpecialFlags": special_flags
		}
		self.layers[lk]["data"] = data
		return data
	
	def render(self, fun=0):
		if self.IncludeDebugOverlays:
			self.blit(self.font.render(f"RenderedObj: {len(self.layers)}", 0, "white"), [0,0], layer=200)
		
		lopop=[]
		for i in self.layerold:
			if not i in self.layers:
				layerdata=self.layerold[i]["data"]
				pos,surfb,sprite=layerdata["Pos"],pg.Surface(layerdata["surf"].get_size()),layerdata["sprite"]
				surfb.fill("black")
				self.layers[f"oo{i}"] = {
					"data": {
						"sprite": sprite,
						"click": {
							0: 0,
							1: 0,
							2: 0,
							"*": 0
						},
						"hovering": 0,
						"distance": 0,
						"AvailabilityCheckIsDisplay": 1,
						"surf": surfb,
						"Pos": pos,
						"Layer": -1,
						"LayerID": f"oo{i}",
						"Clip": 0,
						"Disp": 0,
						"SpecialFlags": 0
					}
				}
				lopop.append(i)
		
		for i in lopop:
			self.layerold.pop(i)

		
		layersorg = {}
		for i, (key, e) in enumerate(sorted(self.layers.items(), key=lambda x: x[1]["data"].get("Layer", 0))):
			layersorg[i + 1] = e
		
		for i in layersorg:
			layerdata=layersorg[i]["data"]

			disp,surf,pos,clip,special_flags=layerdata["Disp"],layerdata["surf"],layerdata["Pos"],layerdata["Clip"],layerdata["SpecialFlags"]

			if fun:
				sizec=random.randint(1,surf.get_width()),random.randint(1,surf.get_height())
				posc=random.randint(0,(surf.get_width()-sizec[0])),random.randint(0,(surf.get_height()-sizec[1]))
				clip=(posc,sizec)
			try:
				if clip:
					sprite = self.display.blit(surf, pos, clip, special_flags=special_flags)
				else:
					sprite = disp.blit(surf, pos, special_flags=special_flags)
			except:
				if clip:
					sprite = self.display.blit(surf, pos, clip, special_flags=special_flags)
				else:
					sprite = self.display.blit(surf, pos, special_flags=special_flags)
		self.layerold=self.layers
		self.layers={}

	def slider(self, pos, value=1, min=0, max=1, anchor="", scale=1, disp="display", id=0):
		if id == 0:
			id = f"Slider-D{value};M{min};MX{max};S{scale};P{pos}"
		if not id in self.sliders:
			self.sliders[id] = value
		val = self.sliders[id]
			
		ca=(max-min)
		sbpos=[pos[0], pos[1]+(20)]
		spos=[val, 0]
		#sdtpos=[ca+20, pos[1]+10]
		
		sd=pg.Surface((30,50))
		sd.fill((0,0,0))
		
		sbd=pg.Surface((ca,10))
		sbd.fill((127,127,127))
		
		settingb=self.blit(sbd, sbpos, anchor=anchor, disp=disp)
		setting=self.blit(sd, [settingb["sprite"].x + spos[0], settingb["sprite"].y],anchor="",disp="display")
		#stdat=self.button(self.res.render(f"{val}", color="black"), sdtpos, disp=settingb)
		
		return [setting["click"][0], self.sliders[id]]