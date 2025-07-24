Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: You pressed Ctrl+C/Delete. Don't do that next time okay?
Cause of error: bad coding skillz

Error Type: KeyboardInterrupt
Error: 

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(signal_sys, globals())
  | Line #: 174

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.true_update()
  | Line #: 527

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.load_render()
  | Line #: 627

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.sprid = self.screen.blit(
  | Line #: 499

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: self.draw_queue[id]                                      = pg.sprite.Sprite(img, x=new_pos[0], y=new_pos[1], z=layer, batch=batch, group=self.layers[layer])
  | Line #: 117

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: self._create_vertex_list()
  | Line #: 333

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\sprite.py
  | Line: self._vertex_list = self.program.vertex_list_indexed(
  | Line #: 503

FrameSummary #9:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\shader.py
  | Line: return self._vertex_list_create(count, mode, indices, None, batch=batch, group=group, **data)
  | Line #: 1505

FrameSummary #10:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\shader.py
  | Line: vlist = domain.create(count, len(indices))
  | Line #: 1441

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: index_start = self.safe_index_alloc(index_count)
  | Line #: 702

FrameSummary #12:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\vertexdomain.py
  | Line: return self.index_allocator.alloc(count)
  | Line #: 674

FrameSummary #13:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyglet\graphics\allocation.py
  | Line: def alloc(self, size: int) -> int:
  | Line #: 92


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!