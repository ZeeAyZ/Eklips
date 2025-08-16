Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: Core Eklips Modules were removed/not found, try reinstalling them through Eklips' github repo.
Cause of error: bad coding skillz

Error Type: ImportError
Error: cannot import name 'singleton' from 'classes' (unknown location). Did you mean: 'Singleton'?

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
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\sprite2d.py
  | Line: super().update(delta)
  | Line #: 44

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\twod\node2d.py
  | Line: super().update(delta)
  | Line #: 27

FrameSummary #6:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\canvasitem.py
  | Line: super().update(delta)
  | Line #: 100

FrameSummary #7:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\node.py
  | Line: self._process(delta)
  | Line #: 44

FrameSummary #8:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.call("_process", delta)
  | Line #: 80

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: return mobj(*args)
  | Line #: 61

FrameSummary #10:
  | Filename: <string>
  | Line: 
  | Line #: 17

FrameSummary #11:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: scene.load()
  | Line #: 115

FrameSummary #12:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: self.add_node(node_data)
  | Line #: 111

FrameSummary #13:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 92

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
  | Line #: 41

FrameSummary #17:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self._init_script()
  | Line #: 50

FrameSummary #18:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.script.init_param(self.properties)
  | Line #: 69

FrameSummary #19:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: exec(script_contents, globals=script_glb,locals=script_glb)
  | Line #: 157

FrameSummary #20:
  | Filename: <string>
  | Line: 
  | Line #: 1


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!