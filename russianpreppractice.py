import random
vocablist = "с, with\nу, near\nв, во +acc, in\nна +acc, onto\nо, об +prep, about\nо, об +acc, against\nк, towards\nза +instr, behind\nиз, from\nот, from\nпо, along\nв, во +prep, in\nна +prep, on\nза +acc, for"
def preppractice():
    y = input("Amount of times to practice? ")
    y = int(y)
    x = 0
    right = 0
    wrong = 0
    while x < y: 
        var = random.choice(['с','у','в, во +acc','на +acc','о, об +prep','о, об +acc','к','за +instr','из','от','по', 'в, во +prep', 'на +prep', 'за +acc'])
        print(var)
        if var == 'с':
            if input("What? ") == "with":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'у':
            if input("What? ") == "near":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'в, во +acc':
            if input("What? ") == "to":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'на +acc':
            if input("What? ") == "onto":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'о, об +acc':
            if input("What? ") == "against":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'о, об +prep':
            if input("What? ") == "about":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'к':
            if input("What? ") == "towards":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'за +instr':
            if input("What? ") == "behind":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'из':
            if input("What? ") == "from":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'от':
            if input("What? ") == "from":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'с':
            if input("What? ") == "with":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'по':
            if input("What? ") == "along":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'в, во +prep':
            if input("What? ") == "in":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'на +prep':
            if input("What? ") == "on":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        elif var == 'за +acc':
            if input("What? ") == "for":
                print("Good!")
                right += 1
            else: 
                print("Stupid!")
                wrong += 1
        x += 1
    print("Amount right:", right)
    print("Amount wrong:", wrong)
    goagain = input("Go again? Y/N: ")
    if goagain.lower() == "y":
        preppractice()
    else: menu()
def menu():
    wow = input("Choose something: ")
    if wow.lower() == "practice" or wow.lower() == "p":
        preppractice()
    elif wow.lower() == "vocab" or wow.lower() == "v":
        print(vocablist)
        menu()
    elif wow.lower() == "quit" or wow.lower() == "q":
        print("Have a good day!")
        exit()
    elif wow.lower() == "help" or wow.lower() == "h":
        print("Tool for practicing basic Russsian prepositions.\nCommands:\n p practice vocab\n v see vocab list\n q quit\n h help")
        menu()
    else:
        print("You have to choose something! Enter h to see a list of commands.")
        menu()
menu()