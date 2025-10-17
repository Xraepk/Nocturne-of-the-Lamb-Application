
def main():
    #Imports
    import os

    #Constants

    #Variables
    user_name = ""
    user_info = ""

    #Functions
    def wipe():
        os.system('cls' if os.name == 'nt' else 'clear')

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
                    user_name = input("\nPlease enter your Username or enter \"R\" to return: ")
                    if user_name.upper() == "R":
                        print("\n...Redirecting...\n")
                        name_accepted = True
                    elif os.path.exists(user_name) and os.path.isfile(user_name):
                        user_file = open(user_name, "r+")
                        user_info = user_file.readlines()
                        user_file.close()
                        print(f"\nHello {user_name}")
                        name_accepted = True
                        intro_over = True
                    else:
                        print("\nUsername not found in system.\n")
            elif has_account.upper() == "N":
                while name_accepted == False:
                    user_name = input("\nPlease enter a Username for your new file or enter \"R\" to return: ")
                    if user_name.upper() == "R":
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




    intro_sequence()



if __name__ == '__main__':
    main()