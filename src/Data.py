import json, sys
from classes import CV

project_file   = "eklips/game.json"
game_bdata     = 0
data_directory = 0
game_name      = 0
cvars          = 0
def _init():
    global project_file,game_bdata,data_directory,game_name,cvars
    game_bdata     = json.loads(open(f"{project_file}").read())
    cvars          = CV.CvarCollection()
    cvars.init_from(game_bdata["cvars"])
    data_directory = cvars.get("directory")
    game_name      = game_bdata["game_name"]
    return cvars

_init()

def mod_data(dir,nam):
    global project_file,game_bdata,data_directory,game_name
    project_file = f"{dir}/game.json"
    _init()
    game_name    = nam 