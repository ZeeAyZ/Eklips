import json

data_directory = "eklips"
game_name      = "Eklips 4"
game_bdata     = json.loads(open(f"{data_directory}/game.json").read())

def mod_data(dir,nam):
    global game_bdata,game_name,data_directory
    game_name      = nam
    data_directory = dir
    game_bdata     = json.loads(open(f"{data_directory}/game.json").read())