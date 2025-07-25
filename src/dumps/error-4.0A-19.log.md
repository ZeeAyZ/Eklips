Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(signal_sys, globals())
  | Line #: 172

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.true_update()
  | Line #: 485

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self._rlayer(self.treechildren, self.parameters["transform"]["pos"].copy())
  | Line #: 626

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: _pos     = self._rlayer(data[i], _pos, layer+1)
  | Line #: 617

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: _pos     = self._rlayer(data[i], _pos, layer+1)
  | Line #: 617

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.screen.render(
  | Line #: 608

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: new_pos = self.get_anchor(
  | Line #: 178

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: new_pos = pos.copy()
  | Line #: 46


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!