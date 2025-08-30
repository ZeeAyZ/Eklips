Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: FileNotFoundError
Error: [Errno 2] No such file or directory: 'None/game.json'

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
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\sprite2d.py
  | Line: super().update(delta)
  | Line #: 44

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\node2d.py
  | Line: super().update(delta)
  | Line #: 28

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: super().update(delta)
  | Line #: 109

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\node.py
  | Line: self._process(delta)
  | Line #: 42

FrameSummary #8:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.call("_process", delta)
  | Line #: 81

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: return mobj(*args)
  | Line #: 62

FrameSummary #10:
  | Filename: <string>
  | Line: 
  | Line #: 13

FrameSummary #11:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: scene.load()
  | Line #: 133

FrameSummary #12:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: self.add_node(node_data)
  | Line #: 110

FrameSummary #13:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 91

FrameSummary #14:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\color_rect.py
  | Line: super().__init__(data,parent)
  | Line #: 41

FrameSummary #15:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: super().__init__(data,parent)
  | Line #: 42

FrameSummary #16:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\node.py
  | Line: super().__init__(data)
  | Line #: 39

FrameSummary #17:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self._onready()
  | Line #: 52

FrameSummary #18:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.call("_onready")
  | Line #: 73

FrameSummary #19:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: return mobj()
  | Line #: 60

FrameSummary #20:
  | Filename: <string>
  | Line: 
  | Line #: 23

FrameSummary #21:
  | Filename: <string>
  | Line: 
  | Line #: 6


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!