Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: console.update(keys_nheld, keys_pressed, globals())
  | Line #: 189

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\conhost.py
  | Line: self.con_panel.draw()
  | Line #: 88

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\shapes.py
  | Line: self._vertex_list.draw(self._draw_mode)
  | Line #: 506

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: self.domain.draw_subset(mode, self)
  | Line #: 136

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: buffer.commit()
  | Line #: 503

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