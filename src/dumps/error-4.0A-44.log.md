Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: KeyError
Error: 'color'

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
  | Line: super().update(delta)
  | Line #: 901

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 511

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().update(delta)
  | Line #: 376

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self._process(delta)
  | Line #: 155

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self.call("_process", delta)
  | Line #: 96

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: return mobj(*args)
  | Line #: 78

FrameSummary #10:
  | Filename: <string>
  | Line: 
  | Line #: 17

FrameSummary #11:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\singleton.py
  | Line: scene.load()
  | Line #: 117

FrameSummary #12:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.add_node(node_data)
  | Line #: 84

FrameSummary #13:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 65

FrameSummary #14:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data,parent)
  | Line #: 596

FrameSummary #15:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data,parent)
  | Line #: 317

FrameSummary #16:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: super().__init__(data)
  | Line #: 140

FrameSummary #17:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self._onready()
  | Line #: 50

FrameSummary #18:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: self.call("_onready")
  | Line #: 88

FrameSummary #19:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: return mobj()
  | Line #: 76

FrameSummary #20:
  | Filename: <string>
  | Line: 
  | Line #: 89

FrameSummary #21:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.w,self.h=self._draw_onto_screen(pos)
  | Line #: 545

FrameSummary #22:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: color   = self.properties["transform"]["color"]
  | Line #: 558


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!