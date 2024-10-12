Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: 'Filesystem' object has no attribute 'reset'
Exceptions (if available): None
Error Type: NameError
Error: name 'Expection' is not defined. Did you mean: 'Exception'?

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 291
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\soleng.py
  | Line: exec(code, gl, lc)
  | Line #: 100
  | Data: None

FrameSummary #3:
  | Filename: <string>
  | Line: 
  | Line #: 25
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 291 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\soleng.py, line 100 in run>, <FrameSummary file <string>, line 25 in <module>>], 'exc_type': <class 'NameError'>, '_str': "name 'Expection' is not defined. Did you mean: 'Exception'?", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': <traceback.TracebackException object at 0x000002A6D1BF2540>, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!