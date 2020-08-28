# name: Nero Denney
# description: very basic text adventure

from helpers import promptYesorNo, promptAorB, promptAorBorC
import time

# Global settings
adultMode = None
hasSword = False

# TODO Create dictionary to map words for under 18s


def startGame():
    # Start game logic reset variables
    global hasSword
    global adultMode
    hasSword = False
    displayIntro()
    if adultMode == None:
        choice_age()
    choice_lake()


def displayIntro():
    print("This is the start of your adventure.")
    print("\"Good\" Luck 👍 \n")
    time.sleep(1)


def choice_age():
    global adultMode
    print("Firstly i need to know something about you.")
    adultMode = promptYesorNo("are you over 18")
    print("Thats great now lets get started.")


def choice_lake():
    print("You awake next to a lake covered in an eerie mist.")
    aOrB = promptAorB(
        "would you like to swim across or walk around", "swim across", "walk around")
    if aOrB == 'a':
        print("""Why would you try to swim across a lake covered in mist!
You start swimming into the mist but obviously get disoriented and lost.
Eventually your arms tire and you give up.

You DIED!""")
        choice_startAgain()
    else:
        print("Whilst walking around the lake you see a sparkle in the bushes.")
        choice_bushsparkle()


def choice_bushsparkle():
    choice = promptAorBorC("investigate the sparkle or continue", "rush to investigate",
                           "have a little look", "nah forget that, keep on walking past")
    if choice == "a":
        print('''You jump through the bushes carelessly and awake a sleeping zombie, because of course that's a great sleeping spot for zombies.
He/she/it eats your brain, disappointed in the size of the meal the zombie returns to sleep.

You DIED!''')
        choice_startAgain()
    elif choice == "b":
        print("You see a sword shining though the bush and decide it will be a great addition to your arsenal so you take it.")
        print("\nGreat sword ⚔ acquired.")
        global hasSword
        hasSword = True
        choice_otherSideOfLake()
    else:
        print("You continue on the path ignoring the allure of the sparkling bush.")
        choice_otherSideOfLake()


def choice_otherSideOfLake():
    global hasSword
    time.sleep(2)
    print("You reached the otherside of the lake.")
    print("There is a cave with smoke bellowing out from the entrance.")
    print("Piles of bones lay around the cave.")
    print("As the smoke clears you spot a shadowy figure approaching from inside the cave.")
    time.sleep(2)
    print("Oh no its a dragon 🦎, and he is running out of the cave towards you.")
    if hasSword:
        # With sword
        choice = promptAorBorC("You need to act fast!", "use your sword",
                               "try something with the skeleton bones", "run away")
        if choice == "a":
            print("You attack and kill the dragon with your Great sword.")
            time.sleep(1)
            print("\nCONGRATULATIONS!\n")
            time.sleep(1)
            print("You climb over the dragons lifeless corpse and enter the cave.")
            time.sleep(1)
            print("Curiosly the smoke is still coming from within the cave.")
            time.sleep(1)
            print(
                "You see a lovely little kitchen with a cake on fire and burning in the oven.")
            time.sleep(1)
            print("It seems the dragon was running away from the fire.")
            time.sleep(1)
            print("You killed an innocent dragon you monster.")
            time.sleep(1)
            print("\nTHE END.....")
            choice_startAgain()
        elif choice == "b":
            result_dragonFetch()
        else:
            result_dragonRun()
    else:
        # Without sword
        choice = promptAorB("You need to act fast!",
                            "try something with the skeleton bones", "run away")
        if choice == "a":
            result_dragonFetch()
        else:
            result_dragonRun()


def result_dragonFetch():
    print("You decide to pick up a bone and throw it as far as possible.")
    print("The dragon gets distracted by the bone and rushes to it.")
    print("He seems to enjoy playing fetch.")
    time.sleep(1)
    print("\nCONGRATULATIONS you now have a pet dragon!\n")
    time.sleep(1)
    print("\nTHE END....")
    choice_startAgain()


def result_dragonRun():
    print("As you run away the dragon tramples you. 😥")
    time.sleep(1)
    print("\nYou DIED!")
    choice_startAgain()


def choice_startAgain():
    # Restart the game prompt
    time.sleep(2)
    print()
    choice = promptYesorNo("would you like to play again")
    if choice == True:
        startGame()
    else:
        print("GOODBYE!")


# START GAME LOOP
startGame()
