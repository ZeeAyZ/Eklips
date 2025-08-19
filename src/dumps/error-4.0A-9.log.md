Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.console.update(engine.keys_nheld, engine.keys_pressed, globals())
  | Line #: 59

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\ConHost.py
  | Line: self.ui.render(
  | Line #: 113

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: lbl.color = color_new
  | Line #: 219

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\__init__.py
  | Line: self.document.set_style(0, len(self.document.text), {"color": color})
  | Line #: 300

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: return super().set_style(0, len(self.text), attributes)
  | Line #: 557

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: self._set_style(start, end, attributes)
  | Line #: 463

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: self.styles.update(attributes)
  | Line #: 560


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!