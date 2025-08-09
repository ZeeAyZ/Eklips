Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: TypeError
Error: unhashable type: 'list'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: singleton.scene.update(singleton.signal_sys, singleton.delta)
  | Line #: 41

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 94

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update(delta)
  | Line #: 91

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.draw()
  | Line #: 560

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.w,self.h=self._draw_onto_screen(pos)
  | Line #: 545

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: return self.screen.render(
  | Line #: 548

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: lbl.font_size = size
  | Line #: 209

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\__init__.py
  | Line: self.document.set_style(0, len(self.document.text), {"font_size": font_size})
  | Line #: 340

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: return super().set_style(0, len(self.text), attributes)
  | Line #: 557

FrameSummary #10:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: self.dispatch_event("on_style_text", start, end, attributes)
  | Line #: 464

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\event.py
  | Line: self._raise_dispatch_exception(event_type, args, handler, exception)
  | Line #: 364

FrameSummary #12:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\event.py
  | Line: raise exception
  | Line #: 432

FrameSummary #13:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\event.py
  | Line: if handler(*args):
  | Line #: 361

FrameSummary #14:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._init_document()
  | Line #: 1619

FrameSummary #15:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._update()
  | Line #: 1588

FrameSummary #16:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: lines = self._get_lines()
  | Line #: 1465

FrameSummary #17:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: glyphs, offsets = self._get_glyphs()
  | Line #: 1438

FrameSummary #18:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\layout\base.py
  | Line: self._document.get_font_runs(dpi=self._dpi),
  | Line #: 1625

FrameSummary #19:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: ft: Font = self.get_font(dpi=dpi)
  | Line #: 566

FrameSummary #20:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\text\document.py
  | Line: return font.load(font_name, font_size, weight=weight, italic=italic, stretch=stretch, dpi=dpi)
  | Line #: 576

FrameSummary #21:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\font\__init__.py
  | Line: if descriptor in font_cache:
  | Line #: 169

FrameSummary #22:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\weakref.py
  | Line: o = self.data[key]()
  | Line #: 156


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!