Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: TypeError
Error: 'NoneType' object is not iterable

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.scene.update(engine.delta)
  | Line #: 43

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: raise error
  | Line #: 126

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 123

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\button.py
  | Line: super().update(delta)
  | Line #: 38

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: self.call("_clicked")
  | Line #: 103

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: return mobj()
  | Line #: 60

FrameSummary #7:
  | Filename: <string>
  | Line: 
  | Line #: 4

FrameSummary #8:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: scene.load()
  | Line #: 133

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: self.add_node(node_data)
  | Line #: 110

FrameSummary #10:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 91

FrameSummary #11:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\color_rect.py
  | Line: super().__init__(data,parent)
  | Line #: 41

FrameSummary #12:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: super().__init__(data,parent)
  | Line #: 42

FrameSummary #13:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\node.py
  | Line: super().__init__(data)
  | Line #: 39

FrameSummary #14:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self._onready()
  | Line #: 52

FrameSummary #15:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.call("_onready")
  | Line #: 73

FrameSummary #16:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: return mobj()
  | Line #: 60

FrameSummary #17:
  | Filename: <string>
  | Line: 
  | Line #: 22


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!