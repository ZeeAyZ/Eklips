import json, sys
from classes import CV

ignore_dirparam = False
try:
    project_file = sys.argv[1]
except:
    project_file = "eklips/game.json" # Change this for your project file
if "--ignore-dirparam" in sys.argv:
    ignore_dirparam = True

game_bdata     = 0
data_directory = 0
game_name      = 0
cvars          = 0
def _init():
    global project_file,game_bdata,data_directory,game_name,cvars
    game_bdata     = json.loads(open(f"{project_file}").read())
    cvars          = CV.CvarCollection()
    cvars.init_from(game_bdata["cvars"])
    if ignore_dirparam:
        data_directory = "/".join(project_file.split("/")[:-1])
        cvars.set("directory", data_directory, data_directory, "directoryParameterModifiedByExecuteParam")
    else:
        data_directory = cvars.get("directory")
    game_name      = game_bdata["game_name"]
    return cvars