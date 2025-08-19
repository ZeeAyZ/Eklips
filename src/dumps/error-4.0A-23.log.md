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
  | Line: self.dispatch_event("on_style_text", start, end, attributes)
  | Line #: 464

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\event.py
  | Line: if handler(*args):
  | Line #: 364

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._update_color(start, end)
  | Line #: 1617

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: box.update_colors(colors, box_start, box_end)
  | Line #: 1500

FrameSummary #10:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: _vertex_list.colors[vertex_start_index:vertex_end_index] = colors[:color_end_index] * vertices_per_char
  | Line #: 596

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: region = buffer.get_region(self.start, self.count)
  | Line #: 100


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!