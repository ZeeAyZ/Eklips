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