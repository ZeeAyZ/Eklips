Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: KeyError
Error: 0

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(Signals, globals())
  | Line #: 169

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 118

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.true_update()
  | Line #: 512

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.load_render()
  | Line #: 581

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.sprid = self.screen.blit(
  | Line #: 494

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\UI.py
  | Line: self.draw_queue[id]                                      = pg.sprite.Sprite(img, x=new_pos[0], y=new_pos[1], z=layer, batch=batch, group=self.layers[layer])
  | Line #: 120


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!