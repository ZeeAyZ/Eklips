Oops! Sol just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: KeyError
Error: 'Pos'

FrameSummary #1:
  | Filename: E:\Code\Sol\Sol 0.211\Sol.py
  | Line: ux.blit(resld.load(f"{resld.resfol}/media/sol/sol.png"), [0,0], scale=2, anchor="cx cy")
  | Line #: 218
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Sol\Sol 0.211\classes\ui.py
  | Line: sprite=pg.rect.Rect((dispd["Pos"][0]+pos[0]-sxo, dispd["Pos"][1]+pos[1]-syo), (surf.get_width(), surf.get_height()))
  | Line #: 474
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Sol\Sol 0.211\Sol.py, line 218 in <module>>, <FrameSummary file E:\Code\Sol\Sol 0.211\classes\ui.py, line 474 in blit>], 'exc_type': <class 'KeyError'>, '_str': "'Pos'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Sol/issues.
Your feedback is important to me!