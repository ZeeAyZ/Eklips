class CvarCollection:
    def __init__(self):
        self.cvars = {}
    
    def get(self, name, fallback=None):
        """Get a cvar's data by its name."""
        if not name in self.cvars:
            self.set(name, fallback, fallback, "FallbackCVar")
        return self.cvars.get(name, {"data":fallback})["data"]

    def get_description(self, name, fallback=None):
        """Get a cvar's description by its name."""
        return self.cvars.get(name, {"description":fallback})["description"]

    def set(self, name, data, default=None, description=None):
        """Set a cvar by its name."""
        old_default = self.cvars.get(name, {"default":default})["default"]
        self.cvars[name] = {
            "type": type(data).__name__,
            "default": old_default,
            "data": data,
            "description": description
        }
    
    def init_from(self, config):
        """
        Data: {
            "??": {
                "type": "bool",
                "default": false,
                "description": "??"
            }
        }
        """
        for entry in config:
            ent_data = config[entry]
            self.set(entry, ent_data["default"], ent_data["default"], ent_data.get("description", None))
