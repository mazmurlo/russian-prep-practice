import random
import json

with open("vocablist.json", "r", encoding='utf-8') as f:
    vocablistnu = json.load(f)

def menu():
    t = None
    wow = input("Choose something: ")
    #switch all this shit to switch statements
    if wow[0].lower() == "p":
        if len(wow) > 2:
            t = int(wow[2:])
        preppractice(t)
    elif wow.lower() == "v":
        #needs to be redone
        for q, a in vocablistnu.items():
            print(q, a)
        menu()
    elif wow.lower() == "q":
        print("Have a good day!")
        exit()
    elif wow.lower() == "h":
        print("Tool for practicing basic Russsian prepositions.\nCommands:\n p x | practice vocab x number of times (x argument optional)\n v   | see vocab list\n q   | quit\n h   | help")
        menu()
    else:
        print("You have to choose something! Enter h to see a list of commands.")
        menu()
def preppractice(y):
    if y is None:
        y = input("Amount of times to practice? ")
    if y == "q" or y == "quit":
        menu()
    y = int(y)
    x = 0
    right = 0
    wrong = 0
    while x < y:
        question, answer = random.choice(list(vocablistnu.items()))
        print(question)
        if input("What? ") == answer:
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
        q = y
        preppractice(q)
    else: menu()
menu()