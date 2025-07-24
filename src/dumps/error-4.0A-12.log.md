Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: interface.flip()
  | Line #: 190

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: label_obj.x, label_obj.y = new_pos
  | Line #: 177

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._set_y(y)
  | Line #: 1074

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._update_translation()
  | Line #: 1078

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: box.update_translation(self._x, self._y, self._z)
  | Line #: 1134

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: _vertex_list.translation[:] = translation * _vertex_list.count
  | Line #: 577

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: def _attribute_getter(self: VertexList) -> Array[float | int]:
  | Line #: 98


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!