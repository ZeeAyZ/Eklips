Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: TypeError
Error: Interface.button() got an unexpected keyword argument 'size'

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
  | Line: barb = self.button(self.res.load(f"{self.res.resfol}/media/ui/scroll_y.png"), [25,25+(data["y"])], anchor="right", size=(20, 40 - (barbIsBig / 2)), scale=2-(sxs-1), disp=sprite)
  | Line #: 203
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 313 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\overlay\console.py, line 48 in draw>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 203 in frame>], 'exc_type': <class 'TypeError'>, '_str': "Interface.button() got an unexpected keyword argument 'size'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!