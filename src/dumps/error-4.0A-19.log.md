Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: OverflowError
Error: cannot convert float infinity to integer

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.clock.get_delta() # Delta time variables
  | Line #: 16

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Clock.py
  | Line: gap             -= int(self.get_time_gap(current_dt, self.time()))
  | Line #: 53


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!