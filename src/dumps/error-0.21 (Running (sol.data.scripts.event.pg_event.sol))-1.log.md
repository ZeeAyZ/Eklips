Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: IndexError
Error: list index out of range

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 273
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\soleng.py
  | Line: exec(code, gl, lc)
  | Line #: 97
  | Data: None

FrameSummary #3:
  | Filename: <string>
  | Line: 
  | Line #: 16
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 273 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\soleng.py, line 97 in run>, <FrameSummary file <string>, line 16 in <module>>], 'exc_type': <class 'IndexError'>, '_str': 'list index out of range', '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!