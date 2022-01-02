# Import system functions
import os 

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
  options=menu.keys()
  for entry in options: 
      print (entry, menu[entry])

# Here we have the system responses to each action
# This is acctually an fucking big mess,
# So pay attention to what you are changing here
  selection=input("Please Select:") 
  if selection =='1':
      os.system("clear") 
      print ("Starting complete upgrade")
      os.system("sudo apt update")
      os.system("sudo apt upgrade")
      os.system("clear")
      print ("Done.")
      input("Press Enter to continue...")
      os.system("clear")
  elif selection == '2': 
      os.system("clear") 
      print ("Attention, this is an potentially destructive action")
      os.system("sleep 1")
      os.system("sudo apt autoremove")
      os.system("clear")
      print ("Done.")
      input("Press Enter to continue...")
      os.system("clear")
  elif selection == '3':
      os.system("clear")
      os.system("sudo apt clean") 
      print ("Done, cache was cleaned.")
      os.system("clear")
      input("Press Enter to continue...")
      os.system("clear")
  elif selection == '4': 
      os.system("clear")
      print ("Farewell.")
      break
  else: 
      print ("Unknown Option Selected!")
      os.system("sleep 1")
      os.system("clear")
