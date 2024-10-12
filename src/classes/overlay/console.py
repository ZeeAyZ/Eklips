import pygame as pg
import time, threading
from classes import ui
from classes.overlay import console, achievement, _overlay

class Console(_overlay.Overlay):
	def __init__(self, ux, res):
		_overlay.Overlay.__init__(self, ux)
		self.ux = ux
		self.res = res
		self.cs = int(round(self.ux.display.get_height() / 2))
		self.cw = self.ux.display.get_width()
		self.y = -self.cs
		self.cmd = {}
		self.dt = 0.00001
		self.d=0
		self.cooldownsh = 0
		self.text = "Sol Engine Console\n\n"
	
	def _show(self):
		if self.cooldownsh == 0:
			self.y = 0
			self.cooldownsh = 5
		else:
			self.cooldownsh -= 0.5
	
	def _hide(self):
		if self.cooldownsh == 0:
			self.y = -self.cs
			self.cooldownsh = 5
		else:
			self.cooldownsh -= 0.5
		
	def _cmd(self, txt):
		self.printf(f"] {txt}")
		txtd=txt.split()
		self.cmd[len(self.cmd)] = txtd
	
	def show(self):
		t=threading.Thread(target=self._show)
		t.start()
		
	def hide(self):
		t=threading.Thread(target=self._hide)
		t.start()
	
	def printf(self, text):
		self.text += text + "\n"
		self.d = len(text.splitlines())
	
	def draw(self, event=None):
		if self.y > -self.cs:
			frame = self.ux.frame((self.cw, self.cs), (0, self.y), id="ConsoleFr", alpha=.5)
			txt = self.res.render(self.text, color="white")
			txts = self.res.render("e")
			self.ux.blit(txt, [20,60], disp=frame, layer=2000000000)
			self.ux.input((50, 50), [0,0], anchor="", id="ConsoleInp", event=event, AlwaysOn=1)
			
			if self.ux.inputs["ConsoleInp"]["return"]:
				if len(self.ux.inputs["ConsoleInp"]["value"].split()) > 0:
					if txt.get_height() > self.cs - (txts.get_height() * 2) - 60:
						frame["FrameObjData"]["y"] += txts.get_height()*self.d
					self._cmd(self.ux.inputs["ConsoleInp"]["value"])
				self.ux.inputs.pop("ConsoleInp")