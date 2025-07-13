data = {}

class Signal:
    def __init__(self, id, nid):
        global data
        self.id    = id
        data[nid]  = {"fired":0,"data":[]}
        self.nid   = nid
    
    def fire(self, *args):
        global data
        data[self.nid]["fired"] = 1
        data[self.nid]["data"]  = args

class SignalHandler:
    def __init__(self):
        self.signals = {}
    
    def add_signal(self, id):
        nid=len(self.signals)
        self.signals[nid] = Signal(id,nid)
        return self.signals[nid]
    
    def get(self):
        global data
        fired_signals = []
        for i in self.signals:
            signal = data[i]
            fired,data=signal["fired"],signal["data"]
            if fired:
                fired_signals.append((i,data))
        return fired_signals