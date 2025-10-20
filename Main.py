
def main():
    #Imports
    import os
    import random



    #Constants, Defaults

    DEFAULT_ROOMS = {
                        "Sanctuary" : "A large open room with rows of pews lining the carpeted floors.",
                        "Kitchen" : """A comfortably sized room with cooking equipment lining the walls and a central
counter poking up through the tiled floors.""",
                        "Parish Hall" : """A large open room designed for children with a few tables for potlucks and
games on top of the colorful carpet patterns of the floor.""",
                        "Confessionals" : """A small room with two identical boxes placed at the end, made for
confessing sins, with a hole between then for secret listening.""",
                        "Crypt" : """A dark room where the bodies of previous pastors lay, watching over the future of
St.Jude's. The electric box is located here.""",
                        "Bell Tower" : """A winding staircase that leads to an open area with dangerously low railing
and the church's bell.""",
                        "Pastor's Study" : """A small room similar to a library, with a desk in the center and all
sorts of books pertaining to religious doctrine."""
                    }
    #This list will eventually be turned into a dict on generation where each NPC's value is their attributes.
    #May use named tuple for that. Haven't decided yet.
    DEFAULT_NPC_LIST = ["Clara", "Jacob", "Janice", "Carter", "Lola", "Walter",
                        "Nora", "Shawn", "Helen", "Lewis", "Violet", "Brad"]

    #The following attributes are definitive and must be included in any preset. You can change the types, as in making
    #hair colors red, blue and green, but hair colors must be included. The numbers beside the defaults are optional
    #percentages for how likely it is that a character will have each attribute. Can be turned off for even spreading.

    DEFAULT_NPC_ATTRIBUTES = {
"Hair Lengths":["Short,Medium,Long"],
"Hair Colors":["Blond,Brown,Black"],
"Shoe Types":["Sneakers,Boots,Sandals"],
"Outer Wear":["Hoodie,Cardigan,None"],
"Shirt Colors":["Black,Blue,Grey,Green,Red,Yellow"],
"Pants Types":["Jeans,Slacks,Sweat Pants"],
"Special Wear":["Glasses,Jewelry"],
"Special Items":["Bible,Flashlight"]
                            }


    #Variables
    user_name = ""
    user_info = ""
    rooms = DEFAULT_ROOMS
    npc_list = DEFAULT_NPC_LIST
    npc_attributes = DEFAULT_NPC_ATTRIBUTES

    #Functions
    def wipe():
        os.system('cls' if os.name == 'nt' else 'clear')

    def print_preset_names():
        wipe()
        global user_name
        with open(user_name, "r") as presets:
            preset_info = presets.readlines()
            print("These are the presets currently active on this account:")
            print(f"\n\t Nocturne of the Lamb (Default)")
            for line in preset_info:
                print(f"\t", line)

    def settings():
        return None

    def write_preset(name, func_rooms=DEFAULT_ROOMS, npc_list=DEFAULT_NPC_LIST, attributes=DEFAULT_NPC_ATTRIBUTES, type="new"):
        global user_name
        if type == "new":
            with open(user_name, "a+") as user_file:
                user_file.write("\n")
                user_file.write(name)
        with open(name, "w") as new_preset_file:
            new_rooms_list = []
            for name, val in func_rooms.items():
                new_rooms_list.append(f"{name}:{val},")
            write_me = f"{"/".join(new_rooms_list)[:-1]}"
            new_preset_file.write(write_me.replace("\n", " "))
            new_preset_file.write("\n")
            for index, npc in enumerate(npc_list):
                if index != len(npc_list) - 1:
                    new_preset_file.write(f"{npc},!")
                else:
                    new_preset_file.write(str(npc))
            if type == "npc" or type == "new":
                new_preset_file.write("\n")
            attributes = dict(attributes)
            new_attribute_list = []
            for item, attribute in attributes.items():
                val = ""
                if type == "new":
                    for word in str(attribute).split(","):
                        val += f"{word},!"
                    val = val[:-1]
                    new_attribute_list.append(f"  {item}:{val},")
                else:
                    val += "  "
                    for word in attribute:
                        if attribute.index(word) == len(attribute) - 1 and list(attributes).index(item) == len(attributes) - 1:
                            if type == "items":
                                val += f"{word}   "
                            else:
                                val += f"{word} "
                        else:
                            val += f"{word},!"
                    val += ""
                    new_attribute_list.append(f"{item}:{val},")
            new_preset_file.write(f"{"/".join(new_attribute_list)[:]}")
        input("\nFile Updated. (Enter) ")

    def read_preset(name, print_values=True):
        with open(name, "r") as current_file:
            current_info = current_file.readlines()
        rooms = {}
        room_info = current_info[0].split(",/")
        for index, pair in enumerate(room_info):
            #if index != len(room_info) - 1:
            parts = pair.split(":")
            val = parts[1]
            rooms[parts[0]] = val

        npc_list = current_info[1].split(",!")

        npc_attributes = {}
        attribute_info = current_info[2].split(",/")
        for pair in attribute_info:
            parts = pair.split(":")[:]
            val = parts[1][2:-2].split(",!")
            npc_attributes[parts[0]] = val
        wipe()
        if print_values:
            print(f"{name} file info: ")
            print("\n\tRooms:")
            for name, info in rooms.items():
                print(f"{name} : {info}")
            print()
            print("\n\tNPC List:", end=" ")
            for index, npc in enumerate(npc_list):
                if index == len(npc_list) - 1:
                    print(npc, end="")
                else:
                    print(npc, end=", ")
            print()
            print("\n\tNPC Attributes:")
            for key, val in npc_attributes.items():
                final_val = ""
                for index, word in enumerate(val):
                    final_val += f" {val[index]},"
                if list(npc_attributes).index(key) == len(npc_attributes) - 1:
                    print(f"{key} : {final_val[:-3]}")
                else:
                    print(f"{key} : {final_val[:-2]}")
        return rooms, npc_list, npc_attributes

    def edit_preset():
        global user_name
        current_preset_name = input("\nEnter "
                                    "the name of the file you wish to inspect or enter \"R\" to return: ").strip()
        with open(user_name, "r+") as preset_file:
            preset_info = preset_file.readlines()
            if current_preset_name.strip().upper() == "R":
                edit_over = True
                print_preset_names()
            elif current_preset_name in preset_info:
                editing_current = True
                while editing_current == True:
                    rooms, npc_list, npc_attributes = read_preset(current_preset_name)
                    #The Actual edit actions
                    changing_preset = True

                    new_rooms = rooms
                    new_npc_list = npc_list
                    new_npc_attributes = npc_attributes
                    print("\nEnter one of the following keywords to edit your preset: ")
                    print("\t\"A\" - Room list")
                    print("\t\"B\" - NPC name list")
                    print("\t\"C\" - Attribute list")
                    print("\tEnter anything else to return")
                    edit_nav = input("Enter: ").strip().upper()

                    if edit_nav == "A":
                        editing_rooms = True
                        wipe()
                        print(f"Enter room names one at a time, then enter a description. "
                              f"Enter \"Done\" when you have finished entering names.\n")
                        new_rooms = {}
                        while editing_rooms == True:
                            room_name = input("Enter Name: ").strip().title()
                            if room_name == "Done":
                                finalize_nav = input("\nDo you want to re-write rooms for this preset? (Y/anything else): ").strip().upper()
                                if finalize_nav == "Y":
                                    write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "room")
                                else:
                                    print("\n...Redirecting...\n")
                                editing_rooms = False
                                print_preset_names()
                            else:
                                room_description = input(f"Enter {room_name} Description: ").strip()
                                new_rooms[room_name] = room_description

                    elif edit_nav == "B":
                        editing_npc_list = True
                        wipe()
                        print(f"Enter NPC names one at a time. Enter \"Done\" when you have finished entering names.\n")
                        new_npc_list = []
                        while editing_npc_list == True:
                            room_name = input("Enter: ").strip().title()
                            if room_name == "Done":
                                finalize_nav = input(
                                    "\nDo you want to re-write NPCs for this preset? (Y/anything else): ").strip().upper()
                                if finalize_nav == "Y":
                                    write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "npc")
                                else:
                                    print("\n...Redirecting...\n")
                                editing_npc_list = False
                            else:
                                new_npc_list.append(room_name)

                    elif edit_nav == "C":
                        editing_attributes = True
                        wipe()
                        print("\nEnter one of the following keywords to edit your attributes: ")
                        print("\t\"A\" - Hair Lengths")
                        print("\t\"B\" - Hair Colors")
                        print("\t\"C\" - Shoe Types")
                        print("\t\"D\" - Outer Wear")
                        print("\t\"E\" - Shirt Colors")
                        print("\t\"F\" - Pants Types")
                        print("\t\"G\" - Special Wear")
                        print("\t\"H\" - Special Items")
                        print("\tEnter anything else to return")
                        edit_nav = input("Enter: ").strip().upper()
                        wipe()
                        change_list = []
                        if edit_nav == "A":
                            print("Enter Hair Lengths one at a time. Enter \"Done\" when you have finished entering Lengths.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Hair Lengths for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Hair Lengths"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "B":
                            print("Enter Hair Colors one at a time. Enter \"Done\" when you have finished entering Colors.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Hair Colors for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Hair Colors"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "C":
                            print("Enter Shoe Types one at a time. Enter \"Done\" when you have finished entering Shoes.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Shoe Types for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Shoe Types"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "D":
                            print("Enter Outer Wear one at a time. Enter \"Done\" when you have finished entering Outer Wear.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Outer Wear for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Outer Wear"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "E":
                            print("Enter Shirt Colors one at a time. Enter \"Done\" when you have finished entering Colors.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Shirt Colors for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Shirt Colors"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "F":
                            print("Enter Pants Types one at a time. Enter \"Done\" when you have finished entering Pants.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Pants Types for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Pants Types"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "G":
                            print("Enter Special Wear one at a time. Enter \"Done\" when you have finished entering Special Wear.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Special Wear for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Special Wear"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "attribute")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                        elif edit_nav == "H":
                            print("Enter Special Items one at a time. Enter \"Done\" when you have finished entering Items.\n")
                            while editing_attributes == True:
                                add_me = input("Enter: ").strip()
                                if add_me.title() == "Done":
                                    finalize_nav = input("Do you want to re-write Special Items for this preset? (Y/anything else): ").strip().upper()
                                    if finalize_nav == "Y":
                                        new_npc_attributes["  Special Items"] = change_list
                                        write_preset(current_preset_name, new_rooms, new_npc_list, new_npc_attributes, "items")
                                        editing_attributes = False
                                    else:
                                        print("\n...Redirecting...\n")
                                        editing_attributes = False
                                else:
                                    change_list.append(add_me)
                    else:
                        editing_current = False
                        print_preset_names()



            else:
                input("\nFile name not recognized. Try again. (Enter)")

    def custom_presets():
        wipe()
        create_over = False
        global user_name
        while create_over == False:
            name_accepted = False
            print_preset_names()
            preset_nav_code = input(f"\nEnter \"C\" to create a new preset, enter \"E\" to edit, or enter anything else to return: ")
            if preset_nav_code.strip().upper() == "C":
                while name_accepted == False:
                    preset_name = input("\nEnter the name of your new preset file or enter \"R\" to return: ")
                    if preset_name.strip().upper() == "R":
                        name_accepted = True
                    elif os.path.exists(preset_name) or os.path.isfile(preset_name):
                        print("\nCannot re-write a pre-existing file. Please try a different file name.\n")
                    else:
                        write_preset(preset_name)
                        name_accepted = True
            elif preset_nav_code.strip().upper() == "E":
                    edit_preset()
            else:
                create_over = True

    def intro_sequence():
        wipe()
        global user_name
        global user_info
        intro_over = False

        while intro_over == False:
            name_accepted = False
            has_account = input("Do you have an account? (Y/N): ")
            if has_account.upper() == "Y":
                while name_accepted == False:
                    user_name = input("\nPlease enter your Username or enter \"R\" to return: ").upper().strip()
                    if user_name == "R":
                        print("\n...Redirecting...\n")
                        name_accepted = True
                    elif os.path.exists(user_name) and os.path.isfile(user_name):
                        user_file = open(user_name, "r+")
                        user_info = user_file.readlines()
                        user_file.close()
                        print(f"\nLogin Successful. Welcome {user_name.title()}! (Enter anything to continue)", end=" ")
                        name_accepted = True
                        intro_over = True
                    else:
                        print("\nUsername not found in system.\n")
            elif has_account.upper() == "N":
                while name_accepted == False:
                    user_name = input("\nPlease enter a new Username or enter \"R\" to return: ").upper().strip()
                    if user_name == "R":
                        print("\n...Redirecting...\n")
                        name_accepted = True
                    elif not(os.path.exists(user_name) or os.path.isfile(user_name)):
                        user_file = open(user_name, "w")
                        user_file.close()
                        name_accepted = True
                    else:
                        print("\nCannot re-write a pre-existing file. Please try a different Username.")
            else:
                print("\nAnswer must be either \"Y\" or \"N\".\n")
        input()
        wipe()

    def start_screen():
        begin = False
        while begin == False:
            wipe()
            nav_code = input("Enter \"ST\" to start, \"SE\" to edit settings, or \"P\" to create custom presets: ")
            nav_code = nav_code.upper()
            if nav_code == "ST":
                begin = True
            elif nav_code == "SE":
                settings()
            elif nav_code == "P":
                custom_presets()
            else:
                print("Input must be \"ST\", \"SE\", or \"P\".\n")

    def generate():
        print_preset_names()
        preset_accepted = False
        global user_name

        generate_rooms = {}
        generate_npcs = []
        generate_attributes = {}

        while preset_accepted == False:
            preset_to_load =  input("\nEnter preset name for generation. (Enter nothing for Default Preset): ").strip()
            with open(user_name, "r") as user_file:
                if preset_to_load.strip() == "":
                    preset_to_load = "Default"
                    preset_accepted = True
                elif preset_to_load in user_file:
                    print("yup")
                    preset_accepted = True
                else:
                    print("Preset name not recognized. Try again.")
        if preset_to_load == "Default":
            for room, description in DEFAULT_ROOMS.items():
                generate_rooms[room.replace("\n", " ")] = description.replace("\n", " ")
            generate_npcs = DEFAULT_NPC_LIST
            for category, section in DEFAULT_NPC_ATTRIBUTES.items():
                final_words = []
                for words in section:
                    for word in words.split(","):
                        final_words.append(word)
                generate_attributes[category] = final_words
        else:
            generate_rooms, generate_npcs, generate_attributes = read_preset(preset_to_load, False)
            
    intro_sequence()
    start_screen()
    generate()


if __name__ == '__main__':
    main()