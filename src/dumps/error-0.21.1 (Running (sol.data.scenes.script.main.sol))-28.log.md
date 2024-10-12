Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: TypeError
Error: '<' not supported between instances of 'int' and 'tuple'

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: solcons.draw(event)
  | Line #: 313
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\overlay\console.py
  | Line: frame = self.ux.frame((self.cw, self.cs), (0, self.y), id="ConsoleFr", alpha=.5)
  | Line #: 48
  | Data: None

FrameSummary #3:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: if aftm > 0 and aftm < size:
  | Line #: 209
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 313 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\overlay\console.py, line 48 in draw>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 209 in frame>], 'exc_type': <class 'TypeError'>, '_str': "'<' not supported between instances of 'int' and 'tuple'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!