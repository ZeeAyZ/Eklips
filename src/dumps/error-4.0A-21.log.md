Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: UnicodeDecodeError
Error: 'charmap' codec can't decode byte 0x8d in position 218: character maps to <undefined>

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
  | Line #: 482

FrameSummary #5:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: self.call_deferred("_process")
  | Line #: 214

FrameSummary #6:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: raise e
  | Line #: 203

FrameSummary #7:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: else: func()
  | Line #: 200

FrameSummary #8:
  | Filename: <string>
  | Line: 
  | Line #: 23

FrameSummary #9:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Nodes.py
  | Line: what = self.resourceman.load(self.parameters["media"]).get()
  | Line #: 324

FrameSummary #10:
  | Filename: E:\Code\Eklips\git\repo\Eklips\src\classes\Resources.py
  | Line: asset = open(actual_path).read()
  | Line #: 220

FrameSummary #11:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\encodings\cp1252.py
  | Line: return codecs.charmap_decode(input,self.errors,decoding_table)[0]
  | Line #: 23


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!