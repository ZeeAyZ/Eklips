Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: FileNotFoundError
Error: [Errno 2] No such file or directory: '../../../../terre/game.json'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: console.update(keys_nheld, keys_pressed, globals())
  | Line #: 192

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self.input(self.input_text)
  | Line #: 119

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: raise error
  | Line #: 200

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self._proccmd(text)
  | Line #: 197

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: exec(f"reload_engine('{args[0]}')", self.eng_gl, self.eng_gl)
  | Line #: 180

FrameSummary #6:
  | Filename: <string>
  | Line: 
  | Line #: 1

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: cvars = Data._init()
  | Line #: 39

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Data.py
  | Line: game_bdata     = json.loads(open(f"{project_file}").read())
  | Line #: 18


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!