Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: TypeError
Error: 'tuple' object does not support item assignment

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: solcons.draw(event)
  | Line #: 313
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\overlay\console.py
  | Line: frame = self.ux.frame((self.cw, self.cs), (0, self.y), id="ConsoleFr", alpha=.5)
  | Line #: 53
  | Data: None

FrameSummary #3:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: barb = self.button(self.res.load(f"{self.res.resfol}/media/ui/scroll_y.png"), [25,25+dys], anchor="right", size=(20, 40 - (barbIsBigd / 2)), scale=2-(sxs-1), disp=sprite)
  | Line #: 209
  | Data: None

FrameSummary #4:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: asset = self.blit(surft, pos, anchor, scale, 0, special_flags, disp=disp, clks=0, frys=frys, size=size)
  | Line #: 304
  | Data: None

FrameSummary #5:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: size[1]=abs(size[1])
  | Line #: 387
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 313 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\overlay\console.py, line 53 in draw>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 209 in frame>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 304 in button>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 387 in blit>], 'exc_type': <class 'TypeError'>, '_str': "'tuple' object does not support item assignment", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!