Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: SyntaxError
Error: invalid syntax. Perhaps you forgot a comma? (<string>, line 81)

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
  | Line #: 39

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
  | Line #: 50

FrameSummary #8:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: scene.load()
  | Line #: 138

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: self.add_node(node_data)
  | Line #: 110

FrameSummary #10:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: object.__init__(node_obj_data, parent)
  | Line #: 91

FrameSummary #11:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\button.py
  | Line: super().__init__(data,parent)
  | Line #: 33

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
  | Line: self._init_script()
  | Line #: 51

FrameSummary #15:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Object.py
  | Line: self.script.init_param(self.properties)
  | Line #: 70

FrameSummary #16:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: exec(script_contents, globals=script_glb,locals=script_glb)
  | Line #: 162
SyntaxError related:
  | Filename: <string>
  | Message: invalid syntax. Perhaps you forgot a comma?
  | Offset: 40
  | EndOffset: 50
  | Text:     lblb.place(relx=1,rely=1, x=-145,y=-55 anchor=tk.SE)

  | Line#: 81
  | End Line#: 81


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!