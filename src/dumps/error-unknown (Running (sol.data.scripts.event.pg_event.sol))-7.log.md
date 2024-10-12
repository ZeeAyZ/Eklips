Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: FileNotFoundError
Error: [Errno 2] No such file or directory: 'sol/data/scenes/script/main.sol'

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 288
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\soleng.py
  | Line: code=open(file).read()
  | Line #: 85
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 288 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\soleng.py, line 85 in run>], 'exc_type': <class 'FileNotFoundError'>, '_str': "[Errno 2] No such file or directory: 'sol/data/scenes/script/main.sol'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!