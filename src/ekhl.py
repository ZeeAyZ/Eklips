import tkinter
import traceback, os
from tkinter import ttk
from tkinter.messagebox import *

ep = 0

class Preview(Exception): #Preview Error Class
	def __none__(self): return None

def rs(vers, ISTRACEBACK): #Raise error
	global ep
	if ISTRACEBACK:
		exp=traceback.TracebackException.from_exception(ep)
		expd=f"""Cause: {exp.__cause__}
Context: {exp.__context__}
Exceptions (if available): {exp.exceptions}
Error Type: {exp.exc_type.__name__}
Error: {exp}
"""
	
		fsid=1
		for i in exp.stack:
			expd+=f"""
FrameSummary #{fsid}:
  | Filename: {i.filename}
  | Line: {i.line}
  | Line #: {i.lineno}
  | Data: {i.locals}
"""
			fsid+=1
	
		try:
			expd+=f"""SyntaxError related:
  | Filename: {exp.filename}
  | Message: {exp.msg}
  | Offset: {exp.offset}
  | EndOffset: {exp.end_offset}
  | Text: {exp.text}
  | Line#: {exp.lineno}
  | End Line#: {exp.end_lineno}
"""
		except:
			pass
		expd+=f"""
Traceback dictionary: {exp.__dict__}
"""
		try:
			os.mkdir("dumps")
		except:
			pass
		fn=f"dumps/error-{vers}-{len(os.listdir('dumps'))+1}.log.md"
	
		qf = "N/A (Not Available)"
		if exp.exc_type.__name__ == "Preview":
			qf = "The Sol Error handler recieved no data, so you got this error."
		elif (exp.exc_type.__name__ == "pygame.error" and exp == "Out of memory") or exp.exc_type.__name__ == "MemoryError":
			qf = "Sol ran out of memory! Try giving the app more memory to work with."
		elif exp.exc_type.__name__ in ["ImportError", "ModuleNotFoundError"]:
			qf = "Core Sol Modules were removed/not found, try reinstalling them through Sol's github repo."
		elif exp.exc_type.__name__ == "KeyboardInterrupt":
			qf = "You pressed Ctrl+C/Delete. Don't do that next time okay?"
	else:
		fn=f"dumps/error-{vers}-{len(os.listdir('dumps'))+1}.log.md"
		qf="N/A (Not Available)"
		expd=f"The Traceback data could not be found. Attached value: {ep}"
	with open(fn, "w") as f:
		f.write("Oops! Eklips just crashed;\nHere's this crash log!\n\n")
		f.write(f"Quick Fix for users: {qf}\n\n")
		f.write(expd)
		f.write("\n\nPlease send this file to the developers of Sol at https://github.com/Za9-118/Eklips/issues.\nYour feedback is important to me!")
	
	showerror(f"Eklips v{vers}", f"Quick fix: {qf}\n\n{expd}")


def error(ver, e, ISTRACEBACK=1):
	global ep
	
	ep = e
	rs(ver, ISTRACEBACK)

if __name__ == "__main__":
	error("", MemoryError("This is not an error, this is a preview"))
