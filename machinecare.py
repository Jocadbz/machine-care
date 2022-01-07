# Import system functions
import os
from time import sleep


class Terminal:

    HEADER = '\033[95m'
    SUCCESS_OK = '\033[94m'
    SUCCESS_CYAN = '\033[96m'
    SUCCESS_GREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    END_C = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

    menu = {
        "1": "Update and upgrade packages",
        "2": "Remove Orphaned packages",
        "3": "Clean Apt cache",
        "4": "Exit"
    }

    def banner(self):

        os.system("clear")

        os.system("echo Server Name - $(hostname) && echo Today is $(date)")

        startm = """
        -------------------------------
        |        MACHINE - CARE       |
        -------------------------------
        """

        print(self.SUCCESS_OK + startm)
        os.system("sleep 4")

    def menushow(self):
        for choice in self.menu.keys():
            print(self.HEADER + choice, self.menu[choice])


# Define each action
def upgrade_system():
    os.system("clear")
    print("Starting complete upgrade")
    os.system("sudo apt update")
    os.system("sudo apt upgrade && echo Done. && sleep 1")
    input("Press Enter to continue...")
    os.system("clear")
    pass


def clear_system_orphanage_package():
    os.system("clear")
    print("Attention, this is an potentially destructive action")
    os.system("sleep 1 && sudo apt autoremove && Done. && sleep 1")
    input("Press Enter to continue...")
    os.system("clear")
    pass


def clear_system_apt_cache():
    os.system("clear && sudo apt clean && echo Done, cache was cleaned.")
    input("Press Enter to continue...")
    os.system("clear")
    pass


def unknown_entry():
    print("Unknown Option Selected!")
    os.system("sleep 1 && clear")
    pass


def exit_function():
    os.system("clear && echo Farewell.")
    pass


# Print epic menu layout
terminal = Terminal()
terminal.banner()
terminal.menushow()

# Finish it later ---\>
# # Start to print menu
# while True:
#     options = menu.keys()
#     for entry in options:
#         print(entry, menu[entry])

# # Here we have the system responses to each action
#     selection = input("Please select: ")
#     if selection == '1':
#         upgrade_system()
#         pass
#     elif selection == '2':
#         clear_system_orphanage_package()
#         pass
#     elif selection == '3':
#         clear_system_apt_cache()
#         pass
#     elif selection == '4':
#         exit_function()
#         break
#     else:
#         unknown_entry()
#         pass
