"""
Guess The Number:
Player is allowed 6 chances to guess a number between 1 and 20.
"""

import random

# generate and store a random integer from 1 to 20
random_num = random.randint(1,20)

# asks for your name and prints game starting statement
name = input("Hello. What is your name? ")
print("Well {}, I am thinking of a number between 1 and 20.".format(str(name)))

# initial counter with guesses left
guesses_left = 6

# inital counter for number of guesses taken
guesses_taken = 1

# list that stores guessed numbers
already_guessed = []

while guesses_left > 0:
    print("\nYou have {} tries.".format(str(guesses_left)))

    # stores player's guess
    guess = input("Take a guess: ")

    # try to see if player's guess can be converted to an integer
    # if not, return back to start of loop for another input
    try:
        guess = int(guess)
    except ValueError:
        print("Try again! That's not a number/integer!")
        continue
    
    # if player's guess is out of range, loop again
    if guess > 20 or guess < 1:
        print("Your guess, {}, is out of range. Try again.".format(str(guess)))
        continue

    # updating numbers that were already guessed so player won't
    # get penalized for guessing the same number multiple times
    if guess in already_guessed:
        print("Hey! You already guessed {}! Try again.".format(str(guess)))
        continue
    else:
        already_guessed.append(guess)
    
    # if guess is correct, end loop
    # otherwise, lower guesses left counter and increase guesses taken counter
    if guess == random_num:
        print("Good job, {}! You guessed my number in {} guesses!".format(name, str(guesses_taken)))
        break
    elif guess > random_num:
        print("{} too high.".format(str(guess)))
        print("The numbers you've guessed so far:")
        print(already_guessed)
        guesses_left -= 1
        guesses_taken += 1
    elif guess < random_num:
        print("{} is too low.".format(str(guess)))
        print("The numbers you've guessed so far:")
        print(already_guessed)
        guesses_left -= 1
        guesses_taken += 1

    # if player runs out of guesses and no matching number,
    # print ending statement with correct number
    if guesses_left == 0 & guess != random_num:
        print("\nNope, sorry. The number I was thinking of was {}.".format(str(random_num)))
        print("Your guesses were:")
        print(already_guessed)

print("Thanks for playing, {}!".format(str(name)))