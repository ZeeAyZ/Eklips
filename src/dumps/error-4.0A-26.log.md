Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: _tkinter.TclError
Error: NULL main window

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
  | Line #: 16

FrameSummary #8:
  | Filename: <string>
  | Line: 
  | Line #: 134

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\tkinter\ttk.py
  | Line: Widget.__init__(self, master, "ttk::button", kw)
  | Line #: 589

FrameSummary #10:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\tkinter\ttk.py
  | Line: tkinter.Widget.__init__(self, master, widgetname, kw=kw)
  | Line #: 534

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\tkinter\__init__.py
  | Line: self.tk.call(
  | Line #: 2780


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!