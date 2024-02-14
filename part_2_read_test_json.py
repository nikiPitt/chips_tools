import test_data
import json

#Creates and returns a GameLibrary object(defined in test_data) from loaded json_data
def make_game_library_from_json( json_data ):
    #Create GameLibrary object
    game_library = test_data.GameLibrary()

    #Iterate through json file
    for key in json_data:
        #Create Game object
        gameToAdd = test_data.Game()
        #Create platform object
        platformToAdd = test_data.Platform()
        #Update Game object field
        gameToAdd.title = json_data[key]['title']
        gameToAdd.year = json_data[key]['year']
        #Update Platform object field
        platformToAdd.name = json_data[key]['platform']['name']
        platformToAdd.launch_year = json_data[key]['platform']['launch_year']
        #Update Game object Platform field using Platform obejct
        gameToAdd.platform = platformToAdd
        #Append Game object to GameLibrary
        game_library.add_game(gameToAdd)

    return game_library

def loadfile():
    #Part 2
    input_json_file = "data/test_data.json"
    #Load json file Python wise
    with open(input_json_file, "r") as f:
        jsonData = json.load(f)
    #Call make_game_library_from_json function
    gameLib = make_game_library_from_json(jsonData)
    #Print the result
    print(gameLib)

loadfile()