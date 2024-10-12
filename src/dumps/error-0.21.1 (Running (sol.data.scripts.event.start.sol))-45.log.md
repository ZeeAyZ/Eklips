Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: AttributeError
Error: 'str' object has no attribute 'get'

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: ux.render()
  | Line #: 314
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: for i, e in enumerate(sorted(self.layers, key=lambda x: x.get("data", {}).get("Layer", 0))):
  | Line #: 526
  | Data: None

FrameSummary #3:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: for i, e in enumerate(sorted(self.layers, key=lambda x: x.get("data", {}).get("Layer", 0))):
  | Line #: 526
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 314 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 526 in render>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 526 in <lambda>>], 'exc_type': <class 'AttributeError'>, '_str': "'str' object has no attribute 'get'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!