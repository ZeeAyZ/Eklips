Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: UnboundLocalError
Error: cannot access local variable 'sprite' where it is not associated with a value

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: ux.render()
  | Line #: 313
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: "sprite": sprite,
  | Line #: 561
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 313 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 561 in render>], 'exc_type': <class 'UnboundLocalError'>, '_str': "cannot access local variable 'sprite' where it is not associated with a value", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!