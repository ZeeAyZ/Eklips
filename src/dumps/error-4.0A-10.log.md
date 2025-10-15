Oops! Eklips just crashed;
Here's this crash log!

Quick Fix for users: N/A (Not Available)
Cause of error: bad coding skillz

Error Type: RecursionError
Error: maximum recursion depth exceeded

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
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #10:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #11:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #12:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #13:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #14:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #15:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #16:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #17:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #18:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #19:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #20:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #21:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #22:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #23:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #24:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #25:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #26:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #27:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #28:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #29:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #30:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #31:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #32:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #33:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #34:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #35:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #36:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #37:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #38:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #39:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #40:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #41:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #42:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #43:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #44:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #45:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #46:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #47:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #48:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #49:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #50:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #51:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #52:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #53:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #54:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #55:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #56:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #57:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #58:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #59:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #60:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #61:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #62:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #63:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #64:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #65:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #66:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #67:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #68:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #69:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #70:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #71:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #72:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #73:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #74:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #75:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #76:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #77:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #78:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #79:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #80:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #81:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #82:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #83:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #84:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #85:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #86:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #87:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #88:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #89:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #90:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #91:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #92:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #93:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #94:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #95:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #96:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #97:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #98:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #99:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #100:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #101:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #102:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #103:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #104:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #105:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #106:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #107:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #108:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #109:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #110:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #111:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #112:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #113:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #114:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #115:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #116:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #117:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #118:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #119:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #120:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #121:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #122:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #123:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #124:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #125:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #126:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #127:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #128:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #129:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #130:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #131:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #132:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #133:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #134:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #135:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #136:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #137:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #138:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #139:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #140:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #141:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #142:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #143:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #144:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #145:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #146:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #147:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #148:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #149:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #150:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #151:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #152:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #153:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #154:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #155:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #156:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #157:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #158:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #159:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #160:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #161:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #162:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #163:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #164:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #165:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #166:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #167:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #168:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #169:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #170:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #171:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #172:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #173:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #174:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #175:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #176:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #177:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #178:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #179:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #180:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #181:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #182:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #183:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #184:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #185:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #186:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #187:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #188:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #189:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #190:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #191:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #192:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #193:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #194:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #195:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #196:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #197:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #198:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #199:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #200:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #201:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #202:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #203:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #204:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #205:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #206:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #207:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #208:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #209:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #210:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #211:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #212:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #213:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #214:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #215:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #216:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #217:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #218:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #219:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #220:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #221:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #222:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #223:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #224:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #225:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #226:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #227:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #228:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #229:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #230:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #231:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #232:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #233:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #234:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #235:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #236:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #237:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #238:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #239:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #240:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #241:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #242:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #243:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #244:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #245:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #246:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #247:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #248:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #249:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #250:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #251:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #252:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #253:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #254:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #255:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #256:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #257:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #258:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #259:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #260:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #261:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #262:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #263:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #264:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #265:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #266:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #267:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #268:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #269:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #270:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #271:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #272:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #273:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #274:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #275:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #276:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #277:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #278:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #279:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #280:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #281:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #282:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #283:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #284:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #285:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #286:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #287:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #288:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #289:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #290:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #291:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #292:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #293:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #294:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #295:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #296:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #297:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #298:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #299:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #300:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #301:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #302:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #303:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #304:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #305:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #306:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #307:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #308:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #309:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #310:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #311:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #312:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #313:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #314:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #315:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #316:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #317:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #318:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #319:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #320:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #321:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #322:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #323:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #324:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #325:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #326:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #327:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #328:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #329:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #330:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #331:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #332:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #333:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #334:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #335:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #336:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #337:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #338:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #339:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #340:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #341:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #342:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #343:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #344:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #345:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #346:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #347:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #348:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #349:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #350:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #351:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #352:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #353:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #354:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #355:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #356:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #357:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #358:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #359:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #360:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #361:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #362:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #363:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #364:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #365:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #366:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #367:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #368:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #369:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #370:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #371:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #372:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #373:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #374:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #375:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #376:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #377:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #378:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #379:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #380:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #381:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #382:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #383:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #384:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #385:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #386:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #387:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #388:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #389:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #390:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #391:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #392:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #393:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #394:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #395:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #396:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #397:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #398:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #399:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #400:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #401:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #402:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #403:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #404:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #405:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #406:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #407:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #408:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #409:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #410:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #411:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #412:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #413:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #414:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #415:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #416:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #417:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #418:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #419:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #420:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #421:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #422:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #423:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #424:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #425:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #426:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #427:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #428:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #429:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #430:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #431:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #432:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #433:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #434:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #435:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #436:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #437:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #438:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #439:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #440:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #441:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #442:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #443:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #444:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #445:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #446:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #447:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #448:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #449:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #450:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #451:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #452:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #453:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #454:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #455:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #456:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #457:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #458:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #459:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #460:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #461:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #462:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #463:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #464:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #465:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #466:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #467:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #468:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #469:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #470:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #471:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #472:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #473:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #474:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #475:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #476:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #477:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #478:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #479:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #480:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #481:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #482:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #483:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #484:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #485:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #486:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #487:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #488:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #489:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #490:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #491:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #492:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #493:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #494:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #495:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #496:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #497:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #498:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #499:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #500:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #501:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #502:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #503:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #504:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #505:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #506:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #507:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #508:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #509:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #510:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #511:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #512:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #513:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #514:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #515:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #516:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #517:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #518:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #519:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #520:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #521:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #522:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #523:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #524:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #525:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #526:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #527:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #528:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #529:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #530:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #531:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #532:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #533:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #534:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #535:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #536:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #537:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #538:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #539:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #540:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #541:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #542:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #543:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #544:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #545:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #546:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #547:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #548:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #549:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #550:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #551:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #552:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #553:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #554:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #555:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #556:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #557:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #558:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #559:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #560:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #561:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #562:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #563:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #564:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #565:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #566:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #567:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #568:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #569:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #570:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #571:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #572:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #573:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #574:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #575:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #576:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #577:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #578:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #579:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #580:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #581:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #582:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #583:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #584:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #585:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #586:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #587:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #588:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #589:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #590:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #591:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #592:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #593:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #594:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #595:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #596:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #597:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #598:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #599:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #600:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #601:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #602:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #603:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #604:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #605:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #606:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #607:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #608:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #609:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #610:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #611:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #612:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #613:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #614:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #615:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #616:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #617:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #618:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #619:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #620:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #621:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #622:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #623:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #624:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #625:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #626:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #627:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #628:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #629:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #630:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #631:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #632:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #633:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #634:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #635:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #636:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #637:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #638:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #639:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #640:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #641:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #642:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #643:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #644:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #645:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #646:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #647:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #648:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #649:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #650:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #651:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #652:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #653:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #654:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #655:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #656:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #657:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #658:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #659:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #660:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #661:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #662:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #663:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #664:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #665:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #666:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #667:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #668:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #669:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #670:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #671:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #672:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #673:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #674:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #675:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #676:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #677:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #678:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #679:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #680:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #681:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #682:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #683:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #684:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #685:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #686:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #687:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #688:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #689:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #690:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #691:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #692:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #693:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #694:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #695:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #696:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #697:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #698:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #699:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #700:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #701:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #702:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #703:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #704:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #705:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #706:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #707:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #708:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #709:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #710:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #711:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #712:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #713:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #714:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #715:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #716:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #717:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #718:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #719:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #720:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #721:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #722:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #723:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #724:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #725:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #726:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #727:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #728:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #729:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #730:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #731:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #732:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #733:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #734:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #735:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #736:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #737:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #738:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #739:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #740:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #741:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #742:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #743:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #744:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #745:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #746:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #747:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #748:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #749:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #750:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #751:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #752:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #753:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #754:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #755:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #756:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #757:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #758:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #759:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #760:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #761:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #762:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #763:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #764:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #765:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #766:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #767:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #768:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #769:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #770:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #771:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #772:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #773:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #774:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #775:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #776:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #777:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #778:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #779:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #780:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #781:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #782:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #783:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #784:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #785:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #786:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #787:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #788:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #789:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #790:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #791:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #792:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #793:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #794:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #795:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #796:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #797:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #798:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #799:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #800:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #801:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #802:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #803:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #804:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #805:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #806:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #807:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #808:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #809:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #810:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #811:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #812:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #813:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #814:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #815:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #816:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #817:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #818:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #819:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #820:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #821:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #822:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #823:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #824:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #825:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #826:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #827:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #828:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #829:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #830:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #831:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #832:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #833:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #834:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #835:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #836:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #837:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #838:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #839:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #840:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #841:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #842:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #843:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #844:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #845:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #846:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #847:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #848:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #849:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #850:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #851:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #852:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #853:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #854:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #855:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #856:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #857:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #858:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #859:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #860:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #861:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #862:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #863:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #864:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #865:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #866:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #867:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #868:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #869:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #870:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #871:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #872:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #873:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #874:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #875:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #876:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #877:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #878:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #879:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #880:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #881:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #882:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #883:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #884:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #885:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #886:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #887:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #888:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #889:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #890:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #891:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #892:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #893:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #894:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #895:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #896:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #897:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #898:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #899:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #900:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #901:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #902:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #903:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #904:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #905:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #906:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #907:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #908:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #909:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #910:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #911:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #912:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #913:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #914:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #915:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #916:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #917:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #918:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #919:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #920:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #921:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #922:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #923:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #924:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #925:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #926:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #927:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #928:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #929:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #930:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #931:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #932:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #933:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #934:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #935:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #936:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #937:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #938:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #939:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #940:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #941:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #942:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #943:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #944:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #945:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #946:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #947:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #948:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #949:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #950:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #951:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #952:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #953:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #954:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #955:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #956:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #957:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #958:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #959:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #960:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #961:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #962:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #963:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #964:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #965:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #966:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #967:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #968:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #969:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #970:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #971:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #972:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #973:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #974:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #975:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #976:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #977:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #978:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #979:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #980:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #981:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #982:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #983:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #984:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #985:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #986:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #987:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #988:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #989:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #990:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #991:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #992:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #993:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #994:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #995:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #996:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #997:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #998:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #999:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #1000:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191

FrameSummary #1001:
  | Filename: D:\Code\Eklips\git\repo\Eklips\src\classes\Singleton.py
  | Line: return ogpopen(args, bufsize, executable,
  | Line #: 191


Please send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. 
Your feedback is important!