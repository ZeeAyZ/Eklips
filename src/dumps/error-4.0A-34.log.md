Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: console.update(keys_nheld, keys_pressed, globals())
  | Line #: 193

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: surf["batch"].draw()
  | Line #: 215

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\__init__.py
  | Line: func()
  | Line #: 558

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: self.program.use()
  | Line #: 216

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\shader.py
  | Line: glUseProgram(self._id)
  | Line #: 1347

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\gl\lib.py
  | Line: error = gl.glGetError()
  | Line #: 70


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!