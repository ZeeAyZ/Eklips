Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: TypeError
Error: Popen.__init__() takes from 2 to 18 positional arguments but 28 were given

FrameSummary #1:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\Eklips.py
  | Line: engine.scene.update(engine.delta)
  | Line #: 58

FrameSummary #2:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: raise error
  | Line #: 148

FrameSummary #3:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Scene.py
  | Line: node.update(delta)
  | Line #: 145

FrameSummary #4:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\media\video_player.py
  | Line: self.play()
  | Line #: 103

FrameSummary #5:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\node\gui\media\video_player.py
  | Line: self.vid        = vid.VideoPyglet(tmp_file_path)
  | Line #: 68

FrameSummary #6:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyvidplayer2\video_pyglet.py
  | Line: Video.__init__(self, path, chunk_size, max_threads, max_chunks, None, post_process, interp, use_pygame_audio, reverse, no_audio, speed, youtube, max_res,
  | Line #: 17

FrameSummary #7:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyvidplayer2\video.py
  | Line: self.no_audio = no_audio or self._test_no_audio()
  | Line #: 185

FrameSummary #8:
  | Filename: C:\Users\ZeeAy\AppData\Local\Programs\Python\Python313\Lib\site-packages\pyvidplayer2\video.py
  | Line: p = subprocess.Popen(command, stdout=subprocess.PIPE, stdin=subprocess.PIPE if self.as_bytes else None)
  | Line #: 434

FrameSummary #9:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(self, args, bufsize, executable,
  | Line #: 191


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!