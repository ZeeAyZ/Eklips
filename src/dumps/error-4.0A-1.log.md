Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: AttributeError
Error: module 'sys' has no attribute '_MEIPASS'

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
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\media\audio_player.py
  | Line: self.play()
  | Line #: 51

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\media\audio_player.py
  | Line: self.audio_data = self.resourceman.load(self.properties["media"]).get()
  | Line #: 41

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: asset    = Sound(f"{sys._MEIPASS}/{actual_path}")
  | Line #: 341


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!