Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: OverflowError
Error: cannot convert float infinity to integer

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
  | Line: self.draw()
  | Line #: 45

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: self._draw_onto_screen(self.image)
  | Line #: 64

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: return self.screen.blit(
  | Line #: 76

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: new_opacity = int(opacity * 255)
  | Line #: 77


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!