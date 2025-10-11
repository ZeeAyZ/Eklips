Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.scene.update(engine.delta)
  | Line #: 43

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 145

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\button.py
  | Line: self.draw()
  | Line #: 42

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\button.py
  | Line: self.w,self.h = self._draw_onto_screen(typ)
  | Line #: 48

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\button.py
  | Line: thmobj = engine.thm.draw_marginable_thing(typ, self.runtime_data["rendererpos"], sz, self.window_id, self.properties["transform"]["anchor"], self.properties["transform"]["layer"])
  | Line #: 69

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: fl = engine.interface.blit(
  | Line #: 238

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: id = f"{path}{cx}{cy}{cw}{ch}"
  | Line #: 94


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!