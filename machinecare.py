# Import system functions
import os
from time import sleep

PRESS_ENTER = "Press Enter to continue..."


class Terminal:

    HEADER = '\033[95m'
    SUCCESS_OK = '\033[94m'
    SUCCESS_CYAN = '\033[96m'
    FAIL = '\033[91m'

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
                    ####################################################################
                    #                           MACHINE - CARE                         #
                    # An simple python script to take care of simple maintenance tasks # 
                    ####################################################################
        """

        print(self.SUCCESS_OK + startm)

        sleep(2)

    def menushow(self):
        # List all available maintenance options the User can choose, see in "menu" dictionary.
        for choice in self.menu.keys():
            print(f"[{self.HEADER + choice}] {self.menu[choice]}")


# Define each action
def upgrade_system():
    os.system("clear")
    print("Starting complete upgrade")
    os.system("sudo apt update")
    os.system("sudo apt upgrade && echo Done. && sleep 1")
    input(PRESS_ENTER)
    os.system("clear")


def clear_system_orphanage_package():
    os.system("clear")
    print("Attention, this is an potentially destructive action")
    os.system("sleep 1 && sudo apt autoremove && Done. && sleep 1")
    input(PRESS_ENTER)
    os.system("clear")


def clear_system_apt_cache():
    os.system("clear && sudo apt clean && echo Done, cache was cleaned.")
    input(PRESS_ENTER)
    os.system("clear")


def unknown_entry():
    print(Terminal.FAIL + "Unknown Option Selected!")
    os.system("sleep 1 && clear")


def exit_function():
    os.system("clear")
    print(Terminal.SUCCESS_CYAN + "Farewell.")
    exit(0)


# Print epic menu layout
# Start to print menu
terminal = Terminal()
terminal.banner()
terminal.menushow()

while True:
    options_dict = {
        "1": upgrade_system, "2": clear_system_orphanage_package,
        "3": clear_system_apt_cache, "4": exit_function
    }

    terminal.menushow()

    selection = input(Terminal.HEADER + "Please select: ")

    # Formatting the input so if the user sends "1  ", it will understand as "1", removing all its whitespaces.
    selection = selection.replace(" ", "")

    if selection in options_dict.keys():
        options_dict[selection]()
    else:
        unknown_entry()
