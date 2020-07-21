# it is a call to a module , so we can use built in methods
import time
# it is a call to a module , so we can use
#  built in methods like random.choice
import random
# Function to pause between messages based on the number of seconds


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(1)

# This function provide the introduction of the game
# Using randomness each time with different scenario


def intro(monster):
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers."
                )
    print_pause(f"Rumor has it that a {monster} is somewhere around here,"
                " and has been terrifying the nearby village."
                )
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective)"
                ",dagger."
                )

# This function be called once the user return back into the field


def caveOrHouse():
    print_pause("Enter 1 to knock on the door of the house.\n")
    print_pause("Enter 2 to peer into the cave.\n")
    print_pause("What would you like to do? \n")

# This function for validating input
# It is a genearal function that we can customze to any prompt


def valid_input(msg, option1, option2):
    while True:
        player_choice = input(msg).lower()
        if option1 == player_choice:
            break
        elif option2 == player_choice:
            break
    return player_choice


# This function if the user choose to enter the cave
# check if the player enter the cave before or not
def cave(monster, enterCaveBefore):
    print_pause("You peer cautiously into the cave")
    if enterCaveBefore is not True:
        print_pause("It turns out to be only a very small cave")
        print_pause("Your eye catches a glint of metal behind a rock")
        print_pause("you have foundthe magical swords")
        print_pause(
            "you discard your silly old dagger and take the sword with you")
        enterCaveBefore = True
        print_pause("You walk back to the field")
        caveOrHouse()
        playerChoice(monster, enterCaveBefore)
    else:
        print_pause("you have been here before, "
                    "and gotten all the good staff.")
        print_pause("It is just an empty cave now.")
        print_pause("you walk about to the field")
        caveOrHouse()
        playerChoice(monster, enterCaveBefore)

# This is a function fight


def fight(monster):
    # Inside the function , randomness will happen to determine
    # wether the player wins or loose
    winOrLoose = random.choice(['win', 'loose'])
    if winOrLoose == 'loose':
        print_pause("You do your best ...")
        print_pause(f"but your dragger is no match for the {monster}")
        print_pause("You have been defeated")
        playAgain()
    else:
        print_pause(f"As the {monster} moves to attack, "
                    "you unsheath your new sowrd."
                    )
        print_pause("The sword shines brightly in your hand"
                    "as you brace yourself for the attack")
        print_pause(f"But the {monster} takes one look at your shiney new toy"
                    "and runs away"
                    )
        print_pause(f"Yoy have rid the town of the {monster}."
                    "You are a victorious")

# Using a function instead of while loop
# to iterate again based on the user choice
        playAgain()


def runaway(monster, enterCaveBefore):
    print_pause("you run back into the field."
                "You don't seem to have been followed"
                )
    caveOrHouse()
    playerChoice(monster, enterCaveBefore)

# if the player has chosen go to house
# house function


def house(monster, enterCaveBefore):
    print_pause("You approach the door of the house")
    print_pause(
        f"You are about to knock when the door opens and out step a{monster}.")
    print_pause(f"Eep! This is a {monster} house")
    print_pause("You feel a bit under_prepared for this,"
                " what with only having a tiny dagger"
                )
# The player choose the way to survive
# after getting into the house
# The player choose Fight or runaway
    survaive = valid_input(
        "Would you like to (1)fight or (2)runaway? \n", '1', '2')
    if survaive == '2':
        # Applying runaway function
        runaway(monster, enterCaveBefore)
    elif survaive == '1':
        # Applying fight function
        fight(monster)


# This function determines the player choice
# The player enters 1 if he wants to go to the house
# The player enters 2 if he wants to go to cave
# Two parameters sent basically from the main function


def playerChoice(randomMonster, hasEnterCave):
    player_choice = valid_input("(Please enter 1 or 2). \n", '1', '2')
    if player_choice == '1':
        house(randomMonster, hasEnterCave)
    elif player_choice == '2':
        cave(randomMonster, hasEnterCave)


# This function is the single entry
#  where the whole game will be kicked off from here

def main():
    monsters = ['dragon', 'fairie', 'pirate']
    randomMonster = random.choice(monsters)
    enterCaveBefore = False
    intro(randomMonster)
    caveOrHouse()
    playerChoice(randomMonster, enterCaveBefore)

# Using a function instead of while loop
#  to iterate again based on the user choice


def playAgain():
    play_agin = valid_input(
        "Would you like to play again? (y/n)\n", 'y', 'n').lower()
    if play_agin == 'y':
        main()
    else:
        print_pause("Thank you, GoodBye!")


# this is the only single line that will motivate the whole game
main()
