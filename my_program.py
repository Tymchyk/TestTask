from bored_module.bored_api import get_response
from bored_module.bd import Database
import sys 

def start (argv):
    # Check if there is no argument
    if argv == []:
        print("You need to add command. Please write 'new' or 'list'!")
        sys.exit()

    # Check if not all arguments included
    if argv[0] == "new" and len(argv) < 13:
        raise TypeError("You need to add all parametrs!")
    
    # Check if there are more arguments than necessary
    if argv[0] == "list" and len(argv) > 1:
        raise TypeError("This command have only one parametrs!")
    
    # Add new activity to table
    if argv[0] == "new":
        argv = sys.argv[2:]
        dict_values = {}
        for i in range(0,len(argv),2):
            dict_values[argv[i].replace("--","")] = argv[i+1]
        data = get_response(**dict_values)
        db.add(data["activity"])
        
    # Return last five values
    if argv[0] == "list":
        data = db.get_value()
        for i,value in enumerate(data, start = 1):
            print(f"{i}. {value[0]}")

if __name__ == "__main__":
    db = Database()
    start(sys.argv[1:])

