import os
import json



# Colourise command line output
class foreground:
    white='\033[39m'
    black='\033[30m'
    yellow='\033[93m'
    pink='\033[95m'
    lightred='\033[91m'
    lightgreen='\033[92m'
    lightcyan='\033[96m'
    lightblue='\033[94m'
    lightgrey='\033[37m'
    darkgrey='\033[90m'



dbFile = input(foreground.pink + "Choose an existing Database file or create a new one:\n")
filename = dbFile + ".json"

if not os.path.exists(filename):
    with open(filename, "w") as f:
        json.dump([], f)
        print(foreground.lightgreen + f"{filename} has been created as your new Database file.")





def print_schema(entry, i):
  info1 = entry["info1"]
  info2 = entry["info2"]
  info3 = entry["info3"]
  print(foreground.lightgreen + f"id: {i} : {info1} : {info2} : {info3}")





def show_menu():
  print(foreground.yellow + "\nSELECT A NUMBER OPTION BELOW AND PRESS ENTER:")
  
  print(foreground.lightcyan + "\n(1)VIEW " + foreground.pink + "(2)SEARCH " + foreground.lightblue + "(3)ADD " + foreground.lightgreen + "(4)EDIT " + foreground.lightred + "(5)DELETE " + foreground.white + "(0)EXIT")





def view_data():
  with open(filename, "r") as f:
    temp = json.load(f)
  i = 0
  for entry in temp:
    print_schema(entry, i)
    i +=1





def search_data():
    search_word = input("Enter search word:\n\n" + foreground.lightgreen).lower()
    with open(filename, "r") as f:
        temp = json.load(f)

    found_results = False  # A flag to check if any results were found

    for i, entry in enumerate(temp):
        info1 = entry["info1"]
        info2 = entry["info2"]
        info3 = entry["info3"]

        if search_word in info1 or search_word in info2 or search_word in info3:
            print(foreground.lightgreen + f"id: {i} : {info1} : {info2} : {info3}")
            found_results = True

    if not found_results:
        print(foreground.lightred + "No results found.")




  
def delete_data():
  view_data()
  new_data = []
  with open(filename, "r") as f:
    temp = json.load(f)
    data_length = len(temp) -1
  delete_option = input(foreground.lightred + f"Select ID to delete from 0-{data_length}\n")
  i = 0
  confirm = input(foreground.lightred + "Are you sure? (Y/N)")
  if confirm == "Y":
    for entry in temp:
      if i == int(delete_option):
        pass
        i +=1
      else:
        new_data.append(entry)
        i +=1
    with open(filename, "w") as f:
      json.dump(new_data, f, indent=4)
    print(foreground.lightgreen + "Deleted successfully")
  else:
      print(foreground.yellow + "No problem. Try another option:")





def edit_data():
  view_data()
  new_data = []
  with open(filename, "r") as f:
    temp = json.load(f)
    data_length = len(temp) -1

  edit_option = input(foreground.yellow + f"Select ID to edit from 0-{data_length}\n")
  i = 0
  confirm = input(foreground.lightred + "Do you wish to proceed? (Y/N)")
  if confirm == "Y":
    for entry in temp:
      if i == int(edit_option):
        print_schema(entry, i)
        info1 = input(f"New info1 (current: {entry['info1']}): ").strip().lower() or entry['info1']
        info1 = info1.lower()
        info2 = input(f"New info2 (current: {entry['info2']}): ").strip().lower() or entry['info2']
        info2 = info2.lower()
        info3 = input(f"New info3 (current: {entry['info3']}): ").strip().lower() or entry['info3']
        info3 = info3.lower()
        new_data.append({"info1": info1, "info2": info2, "info3": info3})
        i +=1
      else:
        new_data.append(entry)
        i +=1
    with open(filename, "w") as f:
      json.dump(new_data, f, indent=4)
  else:
    print(foreground.yellow + "No problem. Try another option:")





def add_data():
  item_data = {}
  with open(filename, "r") as f:
    temp = json.load(f)
  item_data["info1"] = input("Info1: ")
  item_data["info1"] = item_data["info1"].lower()
  item_data["info2"] = input("Info2: ")
  item_data["info2"] = item_data["info2"].lower()
  item_data["info3"] = input("Info3: ")
  item_data["info3"] = item_data["info3"].lower()
  
  temp.append(item_data)
  with open(filename, "w") as f:
    json.dump(temp, f, indent=4)





while True:
  show_menu()
  choice = input("\n")
  if choice == "1":
    view_data()
  elif choice == "2":
    search_data()
  elif choice == "3":
    add_data()
  elif choice == "4":
    edit_data()
  elif choice == "5":
    delete_data()
  elif choice == "0":
    break
  else:
    print(foreground.lightred + "Incorrect option, please try again.")
