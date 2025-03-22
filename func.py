inp="None"

def home():
    print("***************\n")

    print("***************")

    print("N = new task  C = change progress  D = delete task")

    inp=input("> ")


def change_mode(type_from=home(),type_to=None,key=inp):
    match type_from:
        
        case home():
            match key:
                case "n":
                    new()
                
                case "c":
                    change()
                
                case "d":
                    delete()
        case new():
            pass
        case delete():
            pass

    return print("f switched from {type_from} to {type_to}")






class tasks:
    
    def __init__(self,type,progress):
        self.progress=0
        self.type=type_task






