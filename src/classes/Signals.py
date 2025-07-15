data = {}

class Signal:
    """
    A Signal object. This is used to communicate data to other Nodes in a Scene.
    Pass an ID and NID into this class and everything's good to go.
    (An NID is an unique number for each Signal, which, most of the time, is the amount of signals initialized)
    """
    def __init__(self, id, nid):
        global data
        self.id    = id
        data[nid]  = {"fired":0,"data":[]}
        self.nid   = nid
    
    def fire(self, *args):
        """Fire!!"""
        global data
        data[self.nid]["fired"] = 1
        data[self.nid]["data"]  = args
    
    def discard(self):
        """Kills the signal."""
        data.pop(self.nid)
        del self.id
        del self.nid
        del self

class SignalHandler:
    """
    This class handles all signals in the game. It is recommended to use this to make Signals instead of the Signal class.
    """
    def __init__(self):
        self.signals = {}
    
    def add_signal(self, id):
        """Add a signal to the list. Recommended instead of using Signal class. Pass an ID of any kind; String, Int, Float, etc..."""
        nid=len(self.signals)
        self.signals[nid] = Signal(id,nid)
        return self.signals[nid]
    
    def get(self):
        """Get all the fired signals in the handler and empty the list"""
        global data
        fired_signals = []
        for i in self.signals:
            signal = data[i]
            fired,data=signal["fired"],signal["data"]
            if fired:
                fired_signals.append((i,data))
            signal["fired"] = 0
        return fired_signals