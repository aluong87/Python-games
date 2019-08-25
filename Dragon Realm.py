"""
Dragon Realm
Game lets player choose from two choices: 1 or 2.
The outcome is random: either the dragon gives the
player treasure, or eats the player.
"""

# random module for assigning random integer 1 or 2
# time module for delayed text to player
import random
import time

# displays game introduction sequence
def displayIntro():
    print('''
    You are in a land full of dragons. In front of you,
    you see two caves. In one cave, the dragon is friendly
    and will share his treasure with you. The other dragon
    is greedy and hungry, and will eat you on sight.
    ''')

def chosenCave():
    # variable to store player's cave choice of 1 or 2
    cave = ''

    # if player's choice is neither 1 or 2, will ask for choice again
    while cave != '1' and cave != '2':
        cave = input("Which cave will you go into? (1 or 2): ")
    return cave

# function for checking the dragon's cave with player's choice
def checkCave(chosenCave):
    # delayed texts for suspense
    print("You approach the cave...")
    time.sleep(2)
    print("It is dark and spooky...")
    time.sleep(2)
    print("A large dragon jumps out in front of you! He opens his jaws and...")
    time.sleep(2)

    # stores random integer of either 1 or 2
    friendly_dragon = random.randint(1, 2)

    # convert integer of friendly_dragon to string, compare values
    # if player runs into the friendly dragon: treasure!
    # otherwise, death!
    if chosenCave == str(friendly_dragon):
        print("Gives you his treasure!")
    else:
        print("Gobbles you down in one bite!")

# initialize play_again to 'yes' so game will begin
play_again = 'yes'
while play_again == 'yes' or play_again == 'y':
    # begin introduction, store and check player's choice
    displayIntro()
    cave_number = chosenCave()
    checkCave(cave_number)

    # asks player if they wish to play again, converts input to a lower character
    # any other answer will exit the loop, thus ending the game
    play_again = input("\nDo you want to play again? (yes or y to play again): ").lower()

print("Thanks for playing!")    