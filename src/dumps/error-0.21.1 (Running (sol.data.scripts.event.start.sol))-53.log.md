Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: Invalid rectstyle argument
Exceptions (if available): None
Error Type: TypeError
Error: Invalid rectstyle argument

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: ux.render()
  | Line #: 365
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: sprite = self.display.blit(surf, pos, clip, special_flags=special_flags)
  | Line #: 603
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 365 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 603 in render>], 'exc_type': <class 'TypeError'>, '_str': 'Invalid rectstyle argument', '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': <traceback.TracebackException object at 0x000001E54BD51250>, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!