def _turntypeatfirstglance(text):
    """Turn a text input into a type at first glance."""
    try:
        return float(text)
    except ValueError:
        try:
            return int(text)
        except:
            if text.lower() in ["true", "yes", "1", "1.0","y","t","affirmative","ofcourse", "yay", "sure", "ok", "okay"]:
                return True
            elif text.lower() in ["false", "no", "0", "0.0", "none", "nan", "n", "nay", "nope", "nah", "negative"]:
                return False
            else:
                return text

# wtf
def _shift_k(key):
    nk = key.upper()
    if nk == "1": nk = "!"
    if nk == "2": nk = "@"
    if nk == "3": nk = "#"
    if nk == "4": nk = "$"
    if nk == "5": nk = "%"
    if nk == "6": nk = "^"
    if nk == "7": nk = "&"
    if nk == "8": nk = "*"
    if nk == "9": nk = "("
    if nk == "0": nk = ")"
    if nk == "-": nk = "_"
    if nk == "=": nk = "+"
    if nk == "/": nk = "?"
    if nk == "\\": nk = "|"
    if nk == "]": nk = "}"
    if nk == "[": nk = "{"
    if nk == "'": nk = "\""
    if nk == ".": nk = ">"
    if nk == ",": nk = "<"
    if nk == "`": nk = "~"
    if nk == ";": nk = ":"
    return nk