Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: OSError
Error: [WinError 193] %1 is not a valid Win32 application

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
  | Line #: 22

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\subprocess.py
  | Line: self._execute_child(args, executable, preexec_fn, close_fds,
  | Line #: 1039

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\subprocess.py
  | Line: hp, ht, pid, tid = _winapi.CreateProcess(executable, args,
  | Line #: 1554


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!