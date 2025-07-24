Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: AttributeError
Error: 'OptionDialog' object has no attribute 'tk_self'

FrameSummary #1:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.update(Signals, globals())
  | Line #: 171

FrameSummary #2:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.demand_for = []
  | Line #: 118

FrameSummary #3:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: node.update()
  | Line #: 112

FrameSummary #4:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: if not self.dead:
  | Line #: 541

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.call_deferred("on_ready")
  | Line #: 212

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: except Exception as e:
  | Line #: 201

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: func = types.MethodType(self.scriptobj[fun], self)
  | Line #: 198

FrameSummary #8:
  | Filename: <string>
  | Line: 
  | Line #: 18

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: scene.load()
  | Line #: 107

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
  | Line: 
  | Line #: 294


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!