Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: KeyError
Error: 'DNR'

FrameSummary #1:
  | Filename: E:\Code\Sol\git\repo\Sol\src\Sol.py
  | Line: ux.render(fsm.val("Settings/display/FUNMODE"))
  | Line #: 373
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\git\repo\Sol\src\classes\ui.py
  | Line: pos,surfb,sprite,dnr=layerdata["Pos"],pg.Surface(layerdata["surf"].get_size()),layerdata["sprite"],layerdata["DNR"]
  | Line #: 560
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\git\repo\Sol\src\Sol.py, line 373 in <module>>, <FrameSummary file E:\Code\Sol\git\repo\Sol\src\classes\ui.py, line 560 in render>], 'exc_type': <class 'KeyError'>, '_str': "'DNR'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!