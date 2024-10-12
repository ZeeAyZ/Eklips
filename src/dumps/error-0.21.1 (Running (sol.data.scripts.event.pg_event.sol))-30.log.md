Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: TypeError
Error: size must be two numbers

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: sol.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 292
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\soleng.py
  | Line: exec(code, gl, lc)
  | Line #: 100
  | Data: None

FrameSummary #3:
  | Filename: <string>
  | Line: 
  | Line #: 5
  | Data: None

FrameSummary #4:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: asset = self.blit(surft, pos, anchor, scale, 0, special_flags, disp=disp, clks=0, frys=frys, size=size)
  | Line #: 295
  | Data: None

FrameSummary #5:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: surf = pg.transform.scale(surf, size)
  | Line #: 374
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 292 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\soleng.py, line 100 in run>, <FrameSummary file <string>, line 5 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 295 in button>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 374 in blit>], 'exc_type': <class 'TypeError'>, '_str': 'size must be two numbers', '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!