from tkinter.messagebox import *
import traceback, os

class Preview(Exception): #Preview Error Class
    def __none__(self): return None

def report(error):
    pass

ver = "?"

def get_info(error, running):
    global ver
    if error:
        ErrorObject=traceback.TracebackException.from_exception(error)
        ErrorInfo=f"""Error Type: {ErrorObject.exc_type_str}
Error: {ErrorObject}
"""
    
        fsid=1
        for i in ErrorObject.stack:
            ErrorInfo+=f"""
FrameSummary #{fsid}:
  | Filename: {i.filename}
  | Line: {i.line}
  | Line #: {i.lineno}
"""
            fsid+=1
    
        try:
            ErrorInfo+=f"""SyntaxError related:
  | Filename: {ErrorObject.filename}
  | Message: {ErrorObject.msg}
  | Offset: {ErrorObject.offset}
  | EndOffset: {ErrorObject.end_offset}
  | Text: {ErrorObject.text}
  | Line#: {ErrorObject.lineno}
  | End Line#: {ErrorObject.end_lineno}
"""
        except:
            pass
        try:
            os.mkdir("dumps")
        except:
            pass
        fn=f"dumps/error-{ver}-{len(os.listdir('dumps'))+1}.log.md"
    
        QuickFix = "N/A (Not Available)"
        if ErrorObject.exc_type_str == "Preview":
            QuickFix = "The Eklips Error handler recieved no data, so you got this error."
        elif (ErrorObject.exc_type_str == "pygame.error" and ErrorObject == "Out of memory") or ErrorObject.exc_type_str == "MemoryError":
            QuickFix = "Eklips ran out of memory! Try giving the app more memory to work with."
        elif ErrorObject.exc_type_str in ["ImportError", "ModuleNotFoundError"]:
            QuickFix = "Core Eklips Modules were removed/not found, try reinstalling them through Eklips' github repo."
        elif ErrorObject.exc_type_str == "KeyboardInterrupt":
            QuickFix = "You pressed Ctrl+C/Delete. Don't do that next time okay?"
    else:
        fn=f"dumps/error-{ver}-{len(os.listdir('dumps'))+1}.log.md"
        QuickFix="N/A (Not Available)"
        ErrorInfo=f"The Traceback data could not be found. Attached value: {error}"
    with open(fn, "w") as f:
        f.write("Oops! Eklips just crashed;\nHere's this crash log!\n\n")
        f.write(f"Quick Fix for users: {QuickFix}\nCause of error: {running}\n\n")
        f.write(ErrorInfo)
        f.write("\n\nPlease send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. \nYour feedback is important!")
    return ErrorInfo, QuickFix

def raise_error(error, event="unknown", cause_of_event=None):
    info, QuickFix = get_info(error, running=cause_of_event)
    should_i_report = askyesno(
        "Eklips",
        f"Eklips has crashed!\n\n{info}\n\nWould you like to report the error to the developers?\n{QuickFix}"
    )
    if should_i_report:
        report(info)
        askokcancel(
            "Eklips",
            "Thank you for reporting~!"
        )

if __name__ == "__main__":
    raise_error(0)