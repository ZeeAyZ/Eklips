Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: KeyError
Error: ''

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.scene.update(singleton.delta)
  | Line #: 41

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: raise error
  | Line #: 124

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 121

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\progressbar.py
  | Line: self.draw()
  | Line #: 136

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\progressbar.py
  | Line: self._draw_onto_screen(self.bg_img, self.fg_img, int(self.properties["transform"]["size"][0] * (self.properties["value"] / abs(self.properties["maximum"] - self.properties["minimum"]))))
  | Line #: 96

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\progressbar.py
  | Line: self.screen.render(
  | Line #: 124

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: screen       = self.surfaces[blit_in]["screen"]
  | Line #: 164


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!