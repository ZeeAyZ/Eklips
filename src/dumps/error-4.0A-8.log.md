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
  | Line: label_obj.group          = self.layers[layer]
  | Line #: 180

FrameSummary #3:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._update()
  | Line #: 986

FrameSummary #4:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: lines = self._get_lines()
  | Line #: 1465

FrameSummary #5:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: glyphs, offsets = self._get_glyphs()
  | Line #: 1438

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: char_glyphs, char_offsets = font.get_glyphs(text[start:end])
  | Line #: 1633

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\font\dwrite\__init__.py
  | Line: text_layout = self.create_text_layout(text)
  | Line #: 951

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\font\dwrite\__init__.py
  | Line: self._write_factory.CreateTextLayout(
  | Line #: 981

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\libs\win32\com.py
  | Line: return _m(self, *args)
  | Line #: 208


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!