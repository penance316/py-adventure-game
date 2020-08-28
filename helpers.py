# name: Nero Denney
# description: game helper functions

import time

# Answers
requiredText = ("\n !! You entered an invalid answer !!\n")
answer_A = ["A", "a"]
answer_B = ["B", "b"]
answer_C = ["C", "c"]
yes = ["Y", "y", "yes"]
no = ["N", "n", "no"]


def promptUser():
    # Promts user for input
    choice = input(">>> ")
    print()
    time.sleep(0.5)
    return choice


def promptYesorNo(question):
    # Ask yes or no question and return true or false when answered properly.
    print("{0}{1}".format(question.capitalize(), "? (Y or N)"))
    choice = promptUser()
    if choice in yes:
        return True
    elif choice in no:
        return False
    else:
        print(requiredText)
        time.sleep(1)
        return promptYesorNo(question)


def promptAorB(question, choiceA, choiceB):
    # Question with 2 choices.
    print("{0}{1}".format(question.capitalize(), "? (A or B)"))
    print("""
    A: {}
    B: {}
    """.format(choiceA.capitalize(), choiceB.capitalize()))
    choice = promptUser()
    if choice in answer_A:
        return "a"
    elif choice in answer_B:
        return "b"
    else:
        print(requiredText)
        time.sleep(1)
        return promptAorB(question, choiceA, choiceB)


def promptAorBorC(question, choiceA, choiceB, choiceC):
    # Question with 3 choices.
    print("{0}{1}".format(question.capitalize(), "? (A or B or C)"))
    print("""
    A: {}
    B: {}
    C: {}
    """.format(choiceA.capitalize(), choiceB.capitalize(), choiceC.capitalize()))
    choice = promptUser()
    if choice in answer_A:
        return "a"
    elif choice in answer_B:
        return "b"
    elif choice in answer_C:
        return "c"
    else:
        print(requiredText)
        time.sleep(1)
        return promptAorBorC(question, choiceA, choiceB, choiceC)
