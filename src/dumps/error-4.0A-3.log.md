Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: NameError
Error: name 'engineos' is not defined. Did you mean: 'engine'?

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.scene.update(engine.delta)
  | Line #: 40

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: raise error
  | Line #: 124

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 121

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\sprite2d.py
  | Line: super().update(delta)
  | Line #: 44

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\node2d.py
  | Line: super().update(delta)
  | Line #: 27

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: if self.get_if_mouse_hovering():
  | Line #: 91

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: mpos = engineos
  | Line #: 67


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!