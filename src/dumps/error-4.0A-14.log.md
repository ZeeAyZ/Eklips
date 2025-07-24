Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: interface.flip()
  | Line #: 191

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: label_obj.group          = self.layers[layer]
  | Line #: 181

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._update()
  | Line #: 986

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._create_vertex_lists(line.x, line.y, self._anchor_left, anchor_top, line.start, line.boxes, context)
  | Line #: 1481

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: box.place(self, i, self._x, self._y, self._z, line_x, line_y, self._rotation, self._visible, acc_anchor_x,
  | Line #: 2001

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: vertex_list = layout.program.vertex_list_indexed(n_glyphs * 4, GL_TRIANGLES, indices, layout.batch, group,
  | Line #: 499

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\shader.py
  | Line: def vertex_list_indexed(self, count: int, mode: int, indices: Sequence[int], batch: Batch = None,
  | Line #: 1484


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!