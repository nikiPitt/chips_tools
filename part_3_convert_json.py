import cc_dat_utils
import cc_classes
import json


# Part 3
# Load your custom JSON file
# Convert JSON data to CCLevelPack
# Save converted data to DAT file

def make_level_pack_from_json(json_data):
    # Create GameLibrary object
    level_pack = cc_classes.CCLevelPack()

    allLevelData = json_data['levels']

    # Iterate through json file
    for levelData in allLevelData:
        level = cc_classes.CCLevel()

        # Inititate mandatory fields
        level.level_number = levelData["level_number"]
        level.time = levelData["time"]
        level.num_chips = levelData["numberOfChips"]
        level.upper_layer = levelData["upperLayer"]

        # Initiate optional fields
        level.add_field(cc_classes.CCMapTitleField(levelData["map_title"]))
        level.add_field(cc_classes.CCEncodedPasswordField(levelData["password"]))
        level.add_field(cc_classes.CCMapHintField(levelData["hintText"]))

        # Check existence first and initiate the object
        # CLass MonsterMovementField
        if len(levelData["monsters"]) != 0:
            level.add_field(cc_classes.CCMonsterMovementField([cc_classes.CCCoordinate(levelData["monsters"][0][0],
                                                                                       levelData["monsters"][0][1])]))
        # Class TrapControlField
        if ("brown_buttons" in levelData and (levelData["brown_buttons"]) != 0):
            level.add_field(cc_classes.CCTrapControlsField([cc_classes.CCTrapControl(levelData["brown_buttons"][0][0],
                                                                                     levelData["brown_buttons"][0][1],
                                                                                     levelData["brown_buttons"][0][2],
                                                                                     levelData["brown_buttons"][0][3])]))
        # Class CloningMachineControlsField
        if ("red_buttons" in levelData and len(levelData["red_buttons"]) != 0):
            level.add_field(cc_classes.CCCloningMachineControlsField([cc_classes.CCCloningMachineControl(
                                                                                     levelData["red_buttons"][0][0],
                                                                                     levelData["red_buttons"][0][1],
                                                                                     levelData["red_buttons"][0][2],
                                                                                     levelData["red_buttons"][0][3])]))
        # Make total level pack using level objects
        level_pack.levels.append(level)

    return level_pack

def loadfile():
    # Part 2
    input_json_file = "data/nnkim_allLevelData.json"
    # Load json file Python wise
    with open(input_json_file, "r") as f:
        json_data = json.load(f)
    # Call make_game_library_from_json function
    level_pack = make_level_pack_from_json(json_data)
    # Make level pack into dat file
    cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/nnkim_allLevelData.dat")
    print(level_pack);

loadfile()
