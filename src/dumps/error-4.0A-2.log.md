Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: NameError
Error: name 'transform' is not defined

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.scene.update(singleton.delta)
  | Line #: 41

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 98

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update(delta)
  | Line #: 95

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 916

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 498

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 363

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self._process(delta)
  | Line #: 143

FrameSummary #8:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\object.py
  | Line: self.call("_process", delta)
  | Line #: 79

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\object.py
  | Line: return mobj(*args)
  | Line #: 61

FrameSummary #10:
  | Filename: <string>
  | Line: 
  | Line #: 9


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!