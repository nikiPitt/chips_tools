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

    # Iterate through json file
    for key in json_data:
        level = cc_classes.CCLevel()

        # Inititate mandatory fields
        currentlevel = json_data[key]
        level.level_number = currentlevel["level_number"]
        level.time = currentlevel["time"]
        level.num_chips = currentlevel["chip_number"]
        level.upper_layer = currentlevel["upper_layer"]

        # Initiate optional fields
        level.add_field(cc_classes.CCMapTitleField(currentlevel["map_title"]))
        level.add_field(cc_classes.CCEncodedPasswordField(currentlevel["password"]))
        level.add_field(cc_classes.CCMapHintField(currentlevel["hint_text"]))

        # Check existence first and initiate the object
        # CLass MonsterMovementField
        if len(currentlevel["monsters"]) != 0:
            level.add_field(cc_classes.CCMonsterMovementField([cc_classes.CCCoordinate(currentlevel["monsters"][0][0],
                                                                                       currentlevel["monsters"][0][1])]))
        # Class TrapControlField
        if len(currentlevel["brown_buttons"]) != 0:
            level.add_field(cc_classes.CCTrapControlsField([cc_classes.CCTrapControl(currentlevel["brown_buttons"][0][0],
                                                                                     currentlevel["brown_buttons"][0][1],
                                                                                     currentlevel["brown_buttons"][0][2],
                                                                                     currentlevel["brown_buttons"][0][3])]))
        # Class CloningMachineControlsField
        if len(currentlevel["red_buttons"]) != 0:
            level.add_field(cc_classes.CCCloningMachineControlsField([cc_classes.CCCloningMachineControl(
                                                                                     currentlevel["red_buttons"][0][0],
                                                                                     currentlevel["red_buttons"][0][1],
                                                                                     currentlevel["red_buttons"][0][2],
                                                                                     currentlevel["red_buttons"][0][3])]))
        # Make total level pack using level objects
        level_pack.levels.append(level)

    return level_pack

def loadfile():
    # Part 2
    input_json_file = "data/nnkim_cc1.json"
    # Load json file Python wise
    with open(input_json_file, "r") as f:
        json_data = json.load(f)
    # Call make_game_library_from_json function
    level_pack = make_level_pack_from_json(json_data)
    # Make level pack into dat file
    cc_dat_utils.write_cc_level_pack_to_dat(level_pack, "data/nnkim_cc1.dat")

loadfile()
