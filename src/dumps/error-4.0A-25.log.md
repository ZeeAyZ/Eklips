Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: TypeError
Error: argument should be integer or None, not 'tuple'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(signal_sys, globals())
  | Line #: 172

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise error
  | Line #: 121

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.run_script()
  | Line #: 506

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.call_deferred("_process")
  | Line #: 215

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise e
  | Line #: 204

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: else: func()
  | Line #: 201

FrameSummary #8:
  | Filename: <string>
  | Line: 
  | Line #: 18

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.load()
  | Line #: 108

FrameSummary #10:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.add_node(node_data["type"], node_data["path"], node_data["properties"], node_data["script"], node_data, node_data["name"])
  | Line #: 104

FrameSummary #11:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: object.on_ready()
  | Line #: 58

FrameSummary #12:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: asset      = self.resourceman.load(self.parameters["sprite"])
  | Line #: 788

FrameSummary #13:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: assetres = self.load_from_resf(asset)
  | Line #: 220

FrameSummary #14:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: w,h            = f.read(struct.unpack("<II", f.read(8)))
  | Line #: 162


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!