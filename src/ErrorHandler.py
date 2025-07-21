from tkinter.messagebox import *
import traceback, os, webbrowser, requests
from classes.data_ekl import *
from github import Github
from github import Auth

class Preview(Exception): #Preview Error Class
    def __none__(self): return None

error  = None
reason = None

def report(errorinfo, errorobj):
    auth   = Auth.Token(open("../../../../t").read()) # Token.. i'm not putting this in the repo, silly
    g      = Github(auth=auth)
    repo   = g.get_repo("Za9-118/Eklips")
    issuel = 0
    issues = repo.get_issues(state="open")
    for issue in issues:
        if not issue.pull_request:
            issuel += 1
    answer = repo.create_issue(title=f"Automated Issue #{issuel}: {errorobj.exc_type_str}", body=f"{errorinfo}") 

    print(answer)
    g.close()

    return answer

def get_info(error, running):
    global VER
    try:    os.mkdir("dumps")
    except: None
    fn = f"dumps/error-{VER}-{len(os.listdir('dumps'))+1}.log.md"
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
        QuickFix="N/A (Not Available)"
        ErrorInfo=f"The Traceback data could not be found. Attached value: {error}"
    with open(fn, "w") as f:
        f.write("Oops! Eklips just crashed;\nHere's this crash log!\n\n")
        f.write(f"Quick Fix for users: {QuickFix}\nCause of error: {running}\n\n")
        f.write(ErrorInfo)
        f.write("\n\nPlease send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. \nYour feedback is important!")
    return ErrorInfo, QuickFix, ErrorObject

def raise_error(error, event="unknown", cause_of_event=None):
    info, QuickFix, errorobj = get_info(error, running=cause_of_event)
    should_i_report = askyesno(
        "Eklips",
        f"Eklips has crashed!\n\n{info}\n\nFix (if available): {QuickFix}\nAlleged suspect: {event}\nCause of suspect: {cause_of_event}"
    )
    if should_i_report:
        report(info, errorobj)