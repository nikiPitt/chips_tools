import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    game_library = test_data.GameLibrary()

    for key in json_data:
        gameToAdd = test_data.Game()
        platformToAdd = test_data.Platform()
        gameToAdd.title = json_data[key]['title']
        gameToAdd.year = json_data[key]['year']
        platformToAdd.name = json_data[key]['platform']['name']
        platformToAdd.launch_year = json_data[key]['platform']['launch_year']
        gameToAdd.platform = platformToAdd
        game_library.add_game(gameToAdd)

    return game_library

def loadfile():
    #Part 2
    input_json_file = "data/test_data.json"
    with open(input_json_file, "r") as f:
        jsonData = json.load(f)
    gameLib = make_game_library_from_json(jsonData)
    print(gameLib)

loadfile()