Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: ctypes.ArgumentError
Error: argument 2: TypeError: 'float' object cannot be interpreted as an integer

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(signal_sys, globals())
  | Line #: 172

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 121

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.true_update()
  | Line #: 509

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.load_render()
  | Line #: 801

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.sprid = self.screen.blit(
  | Line #: 457

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: spr.image    = img
  | Line #: 136

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: self._set_texture(img.get_texture())
  | Line #: 489

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\image\__init__.py
  | Line: self._current_texture = self.create_texture(Texture)
  | Line #: 650

FrameSummary #10:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\image\__init__.py
  | Line: self.blit_to_texture(texture.target, texture.level, self.anchor_x, self.anchor_y, 0, None)
  | Line #: 644

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\image\__init__.py
  | Line: self._apply_region_unpack()
  | Line #: 741

FrameSummary #12:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\image\__init__.py
  | Line: glPixelStorei(GL_UNPACK_SKIP_PIXELS, self.x)
  | Line #: 948


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!