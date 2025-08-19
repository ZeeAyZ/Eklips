Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: ValueError
Error: invalid literal for int() with base 10: '1755565615.1337316'

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.clock.get_delta() # Delta time variables
  | Line #: 16

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Clock.py
  | Line: current_dt       = int(f"{self._time}")
  | Line #: 46


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!