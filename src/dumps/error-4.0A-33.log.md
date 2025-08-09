Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: FileNotFoundError
Error: [Errno 2] No such file or directory: 'E:/Code/Eklips/Terrestrial/terre/game.json/game.json'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.console.update(singleton.keys_nheld, singleton.keys_pressed, globals())
  | Line #: 61

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self.input(self.input_text)
  | Line #: 137

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: raise error
  | Line #: 225

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self._proccmd(text)
  | Line #: 222

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: exec(f"singleton.reload_engine('{args[0]}')", self.eng_gl, self.eng_gl)
  | Line #: 196

FrameSummary #6:
  | Filename: <string>
  | Line: 
  | Line #: 1

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\singleton.py
  | Line: cvars = Data._init()
  | Line #: 45

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Data.py
  | Line: game_bdata     = json.loads(open(f"{project_file}").read())
  | Line #: 18


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!