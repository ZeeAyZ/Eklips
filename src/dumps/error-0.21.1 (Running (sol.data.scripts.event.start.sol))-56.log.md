Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: AttributeError
Error: 'NoneType' object has no attribute 'get_size'

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: setdisp(1,SpSc=resld.load(f"{resld.resfol}/{fsm.val('Settings/load/splash')}.png"))
  | Line #: 233
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: display = pg.display.set_mode(SpSc.get_size(), pg.NOFRAME)
  | Line #: 28
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 233 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 28 in setdisp>], 'exc_type': <class 'AttributeError'>, '_str': "'NoneType' object has no attribute 'get_size'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!