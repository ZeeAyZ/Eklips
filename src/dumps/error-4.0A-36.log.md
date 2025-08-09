Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: FileNotFoundError
Error: [Errno 2] No such file or directory: 'eklips/data/scenes/curr_project.ekl'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.scene.update(singleton.signal_sys, singleton.delta)
  | Line #: 41

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 98

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update(delta)
  | Line #: 95

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.call("_clicked")
  | Line #: 675

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: return mobj()
  | Line #: 57

FrameSummary #6:
  | Filename: <string>
  | Line: 
  | Line #: 5

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\singleton.py
  | Line: scene.load()
  | Line #: 117

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: scene_obj  = json.loads(self.resourceman.load(self.file_path).get())
  | Line #: 80

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: asset    = open(actual_path).read()
  | Line #: 512


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!