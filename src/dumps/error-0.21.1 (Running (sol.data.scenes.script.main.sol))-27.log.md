Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: ValueError
Error: Cannot scale to negative size

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 288
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\soleng.py
  | Line: exec(code, gl, lc)
  | Line #: 100
  | Data: None

FrameSummary #3:
  | Filename: <string>
  | Line: 
  | Line #: 3
  | Data: None

FrameSummary #4:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: surf = pg.transform.scale(surf, (int(surf.get_width() * scale), int(surf.get_height() * scale)))
  | Line #: 375
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 288 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\soleng.py, line 100 in run>, <FrameSummary file <string>, line 3 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 375 in blit>], 'exc_type': <class 'ValueError'>, '_str': 'Cannot scale to negative size', '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!