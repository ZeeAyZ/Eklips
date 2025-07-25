Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: interface.flip()
  | Line #: 193

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: surf["batch"].draw()
  | Line #: 210

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\__init__.py
  | Line: func()
  | Line #: 558

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\__init__.py
  | Line: draw_list.append((lambda d, m: lambda: d.draw(m))(domain, mode))  # noqa: PLC3002
  | Line #: 488

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: buffer.commit()
  | Line #: 718

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexbuffer.py
  | Line: glBindBuffer(GL_ARRAY_BUFFER, self.id)
  | Line #: 260

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\gl\lib.py
  | Line: error = gl.glGetError()
  | Line #: 70


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!