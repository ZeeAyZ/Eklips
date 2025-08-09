Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: TypeError
Error: can't multiply sequence by non-int of type 'float'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.scene.update(singleton.signal_sys, singleton.delta)
  | Line #: 41

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 96

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update(delta)
  | Line #: 93

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 905

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 511

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 438

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self._process(delta)
  | Line #: 154

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self.call("_process", delta)
  | Line #: 77

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: return mobj(*args)
  | Line #: 59

FrameSummary #10:
  | Filename: <string>
  | Line: 
  | Line #: 17

FrameSummary #11:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\singleton.py
  | Line: scene.load()
  | Line #: 111

FrameSummary #12:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.add_node(node_data)
  | Line #: 82

FrameSummary #13:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 63

FrameSummary #14:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data,parent)
  | Line #: 604

FrameSummary #15:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data,parent)
  | Line #: 384

FrameSummary #16:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data)
  | Line #: 138

FrameSummary #17:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self._onready()
  | Line #: 49

FrameSummary #18:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self.call("_onready")
  | Line #: 69

FrameSummary #19:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: return mobj()
  | Line #: 57

FrameSummary #20:
  | Filename: <string>
  | Line: 
  | Line #: 117

FrameSummary #21:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 63

FrameSummary #22:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data,parent)
  | Line #: 659

FrameSummary #23:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raw_data = bytes([r, g, b] * self.properties["transform"]["size"][0] * self.properties["transform"]["size"][1])
  | Line #: 607


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!