Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)

Cause: None
Context: None
Exceptions (if available): None
Error Type: AttributeError
Error: 'str' object has no attribute '__traceback__'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: ekl.run(f"{resld.resfol}/data/scenes/script/{data['Engine']['Scene']}.sol",gl=globals(),lc=locals())
  | Line #: 350
  | Data: None

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\ekeng.py
  | Line: exec(code, gl, lc)
  | Line #: 100
  | Data: None

FrameSummary #3:
  | Filename: <string>
  | Line: 
  | Line #: 35
  | Data: None

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\ekhl.py
  | Line: rs(ver)
  | Line #: 76
  | Data: None

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\ekhl.py
  | Line: exp=traceback.TracebackException.from_exception(ep)
  | Line #: 13
  | Data: None

FrameSummary #6:
  | Filename: E:\Programs\Python\Lib\traceback.py
  | Line: return cls(type(exc), exc, exc.__traceback__, *args, **kwargs)
  | Line #: 854
  | Data: None

Traceback dictionary: {'max_group_width': 15, 'max_group_depth': 10, 'stack': [<FrameSummary file E:\Code\Eklips\git\repo\Eklips\src\Eklips.py, line 350 in <module>>, <FrameSummary file E:\Code\Eklips\git\repo\Eklips\src\classes\ekeng.py, line 100 in run>, <FrameSummary file <string>, line 35 in <module>>, <FrameSummary file E:\Code\Eklips\git\repo\Eklips\src\ekhl.py, line 76 in error>, <FrameSummary file E:\Code\Eklips\git\repo\Eklips\src\ekhl.py, line 13 in rs>, <FrameSummary file E:\Programs\Python\Lib\traceback.py, line 854 in from_exception>], 'exc_type': <class 'AttributeError'>, '_str': "'str' object has no attribute '__traceback__'", '__notes__': None, '__suppress_context__': False, '__cause__': None, '__context__': None, 'exceptions': None}


Please send this file to the developers of Sol at https://github.com/Za9-118/Eklips/issues.
Your feedback is important to me!