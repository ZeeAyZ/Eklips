class CvarCollection:
    def __init__(self):
        self.cvars = {}
    
    def get(self, name, fallback=None):
        """Get a cvar by its name."""
        return self.cvars.get(name, fallback)

    def set(self, name, data):
        """Set a cvar by its name."""
        self.cvars[name] = data