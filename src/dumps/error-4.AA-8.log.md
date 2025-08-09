Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: NameError
Error: name 'reload_engine' is not defined

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.console.update(singleton.keys_nheld, singleton.keys_pressed, globals())
  | Line #: 61

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self.input(self.input_text)
  | Line #: 120

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: raise error
  | Line #: 207

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self._proccmd(text)
  | Line #: 204

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: exec("reload_engine()", self.eng_gl, self.eng_gl)
  | Line #: 183

FrameSummary #6:
  | Filename: <string>
  | Line: 
  | Line #: 1


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!