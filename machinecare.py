# Import system functions
import os 

# Define each action
def upgrade_system():
    os.system("clear")
    print("Starting complete upgrade")
    os.system("sudo apt update")
    os.system("sudo apt upgrade")
    os.system("clear")
    print("Done.")
    input("Press Enter to continue...")
    os.system("clear")
    pass

def clear_system_orphanage_package():
    os.system("clear")
    print("Attention, this is an potentially destructive action")
    os.system("sleep 1")
    os.system("sudo apt autoremove")
    os.system("clear")
    print("Done.")
    input("Press Enter to continue...")
    os.system("clear")
    pass

def clear_system_apt_cache():
    os.system("clear")
    os.system("sudo apt clean")
    print("Done, cache was cleaned.")
    os.system("clear")
    input("Press Enter to continue...")
    os.system("clear")
    pass

def unknown_entry():
    print("Unknown Option Selected!")
    os.system("sleep 1")
    os.system("clear")
    pass

def exit_function():
    os.system("clear")
    print("Farewell.")
    pass

# Print epic menu layout
# Start to print menu
menu = {}
os.system("clear")
os.system("echo Server Name - $(hostname)")
os.system("echo Today is $(date)")
print ("-------------------------------")
print ("         MACHINE - CARE        ")
print ("-------------------------------")
menu['1']="Update and upgrade packages" 
menu['2']="Remove Orphaned packages"
menu['3']="Clean Apt cache"
menu['4']="Exit"
while True:
  options = menu.keys()
  for entry in options: 
      print(entry, menu[entry])

# Here we have the system responses to each action 
  selection = input("Please select: ")
  if selection =='1':
      upgrade_system()
      pass
  elif selection == '2': 
      clear_system_orphanage_package()
      pass
  elif selection == '3':
      clear_system_apt_cache()
      pass
  elif selection == '4': 
      exit_function()
      break
  else:
      unknown_entry()
      pass


