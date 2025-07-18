Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: program:/internal/loading.scn

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(Signals, globals())
  | Line #: 158

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 113

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.true_update()
  | Line #: 498

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.load_render()
  | Line #: 651

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.screen.blit(
  | Line #: 459

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: new_pos      = self.get_anchor(pos,win_w,win_h,anchor,new_surface.width,new_surface.height,1)
  | Line #: 98

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: return h if self._subpixel else int(h)
  | Line #: 726


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!