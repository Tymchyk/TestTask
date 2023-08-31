from bored_module.bored_api import get_response
from bored_module.bd import Database
import sys 

def start ():
    if sys.argv[1:] == []:
        print("You need to add command. Please write 'new' or 'list'!")
        sys.exit()
    
    if sys.argv[1] == "new" and len(sys.argv[1:]) < 13:
        print("You need to add all parametrs!")
        sys.exit()
    if sys.argv[1] == "list" and len(sys.argv[1:]) > 1:
        print("This command have only one parametrs!")
        sys.exit()
    
    if sys.argv[1] == "new":
        argv = sys.argv[2:]
        dict_values = {}
        for i in range(0,len(argv),2):
            dict_values[argv[i].replace("--","")] = argv[i+1]
        data = get_response(**dict_values)
        try:
            db.add(data["activity"])
        except KeyError:
            print()
    if sys.argv[1] == "list":
        data = db.get_value()
        for i,value in enumerate(data, start = 1):
            print(f"{i}. {value[0]}")
if __name__ == "__main__":
    db = Database()
    start()

