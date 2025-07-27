Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: AttributeError
Error: 'Image' object has no attribute 'get_texture'

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
  | Line #: 514

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.load_render()
  | Line #: 792

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.sprid = self.screen.blit(
  | Line #: 453

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: spr.image    = img
  | Line #: 135

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: self._set_texture(img.get_texture())
  | Line #: 489


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!