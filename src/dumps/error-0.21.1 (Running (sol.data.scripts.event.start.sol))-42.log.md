Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: 'Pos'
Exceptions (if available): None
Error Type: UnboundLocalError
Error: cannot access local variable 'sprite' where it is not associated with a value

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: ux.blit(resld.load(f"{resld.resfol}/media/sol/sol.png"), [0,0], scale=2, anchor="cx cy")
  | Line #: 218
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: spritehb=sprite
  | Line #: 454
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 218 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 454 in blit>], 'exc_type': <class 'UnboundLocalError'>, '_str': "cannot access local variable 'sprite' where it is not associated with a value", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': <traceback.TracebackException object at 0x0000020672DC4560>, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!