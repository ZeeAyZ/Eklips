Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: OSError
Error: [Errno 22] Invalid argument: 'program:/internal/loading.scn'

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
  | Line: scene.load()
  | Line #: 97

FrameSummary #8:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: scene_obj  = json.loads(self.resourceman.load(self.file_path).get())
  | Line #: 80

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: asset    = open(actual_path).read()
  | Line #: 512


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!