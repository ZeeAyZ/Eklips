Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: KeyError
Error: 'rot'

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.scene.update(engine.delta)
  | Line #: 43

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: raise error
  | Line #: 126

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 123

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\media\video_player.py
  | Line: super().update(delta)
  | Line #: 91

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: if self.get_if_mouse_hovering():
  | Line #: 98

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: x,y  = self.screen.get_anchor(self.properties["transform"]["pos"], self.window_id, self.properties["transform"]["anchor"], self.w, self.h, True, self.properties["transform"]["rot"], True)
  | Line #: 71


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!