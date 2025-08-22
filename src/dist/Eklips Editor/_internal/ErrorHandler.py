from tkinter.messagebox import *
import traceback, os, webbrowser, requests
from classes.Constants import *
try:
    from github import Github
    from github import Auth
    can_use_git = True
except:
    can_use_git = False
    print("WARNING: Unable to use Github API")

class Preview(Exception): #Preview Error Class
    def __none__(self): return None

error  = None
reason = None

def report(error_info, errorobj):
    auth   = Auth.Token(open("../../../../t").read()) # Token.. i'm not putting this in the repo, silly
                                                      # Don't ask what the hell this is
    g      = Github(auth=auth)
    repo   = g.get_repo("Za9-118/Eklips")
    issuel = 0
    issues = repo.get_issues(state="open")
    for issue in issues:
        if not issue.pull_request:
            issuel += 1
    answer = repo.create_issue(title=f"Automated Issue #{issuel}: {errorobj.exc_type_str}", body=f"{error_info}") 

    print(answer)
    g.close()

    return answer

def get_info(error, running, save_logs):
    global VER
    try:
        os.mkdir("dumps")
    except:
        pass

    fn = f"dumps/error-{VER}-{len(os.listdir('dumps'))+1}.log.md"
    if error:
        error_obj=traceback.TracebackException.from_exception(error)
        error_info=f"""Error Type: {error_obj.exc_type_str}
Error: {error_obj}
"""
    
        fsid=1
        for i in error_obj.stack:
            error_info+=f"""
FrameSummary #{fsid}:
  | Filename: {i.filename}
  | Line: {i.line}
  | Line #: {i.lineno}
"""
            fsid+=1
    
        try:
            error_info+=f"""SyntaxError related:
  | Filename: {error_obj.filename}
  | Message: {error_obj.msg}
  | Offset: {error_obj.offset}
  | EndOffset: {error_obj.end_offset}
  | Text: {error_obj.text}
  | Line#: {error_obj.lineno}
  | End Line#: {error_obj.end_lineno}
"""
        except:
            pass
    
        quick_fix = "N/A (Not Available)"
        if error_obj.exc_type_str == "Preview" or len(" ".join(error_info.split())) == 0:
            quick_fix = "The Eklips Error handler recieved no data, so you got this error."
        elif (error_obj.exc_type_str == "pygame.error" and error_obj == "Out of memory") or error_obj.exc_type_str == "MemoryError":
            quick_fix = "Eklips ran out of memory! Try giving the app more memory to work with."
        elif error_obj.exc_type_str in ["ImportError", "ModuleNotFoundError"]:
            quick_fix = "Core Eklips Modules were removed/not found, try reinstalling them through Eklips' github repo."
        elif error_obj.exc_type_str == "KeyboardInterrupt":
            quick_fix = "You pressed Ctrl+C/Delete. Don't do that next time okay?"
    else:
        quick_fix="N/A (Not Available)"
        error_info=f"The Traceback data could not be found. Attached value: {error}"
    
    if save_logs:
        with open(fn, "w") as f:
            f.write("Oops! Eklips just crashed;\nHere's this crash log!\n\n")
            f.write(f"Quick Fix for users: {quick_fix}\nCause of error: {running}\n\n")
            f.write(error_info)
            f.write("\n\nPlease send this file to the developers of Eklips at https://github.com/Za9-118/Eklips/issues. \nYour feedback is important!")
    
    return error_info, quick_fix, error_obj

def raise_error(error, event="unknown", cause_of_event=None, save_logs=True):
    error_info, quick_fix, error_obj = get_info(error, running=cause_of_event, save_logs=save_logs)
    if can_use_git:
        should_i_report = askyesno(
            "Eklips",
            f"Eklips has crashed!\n\n{error_info}\n\nFix (if available): {quick_fix}\nAlleged suspect: {event}\nCause of suspicion: {cause_of_event}\n\nWould you like to report this error?"
        )
        if should_i_report:
            report(error_info, error_obj)
    else:
        showerror(
            "Eklips",
            f"Eklips has crashed!\n\n{error_info}\n\nFix (if available): {quick_fix}\nAlleged suspect: {event}\nCause of suspicion: {cause_of_event}"
        )

if __name__ == "__main__":
    raise_error(Preview("Preview"), event="User who is a silly and danger", cause_of_event="You opened ErrorHandler.py", save_logs=False)