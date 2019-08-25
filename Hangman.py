'''
Hangman
Player has up to 8 chances to guess the secret word depending on difficulty chosen.
'''
import random

# picture board (chances)
hangman_pics = ['''
    +---+
        |
        |
        |
       ===''', '''
    +---+
    O   |
        |
        |
       ===''', '''
    +===+
    O   |
    |   |
        |
       ===''', '''
    +---+
    O   |
   /|   |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
        |
       ===''', '''
    +---+
    O   |
   /|\  |
   /    |
       ===''', '''
    +---+
    O   |
   /|\  |
   / \  |
       ===''', '''
    +===+
   [O   |
   /|\  |
   / \  |
       ===''', '''
   [O]  |
   /|\  |
   / \  |
       ===''']

# dictionary of secret words, separated by categories
words = {
    'Colors': 'red orange yellow green blue indigo violet white black brown'.split(),
    'Shapes': '''
    square triangle rectangle circle ellipse rhombus trapezoid chevron pentagon
    hexagon septagon octagon
    '''.split(),
    'Fruits': '''
    apple orange lemon lime pear watermelon grape grapefruit cherry banana
    cantaloupe mango strawberry tomato
    '''.split(),
    'Animals': '''
    bat bear beaver cat cougar crab deer dog donkey duck eagle fish frog goat leech
    lion lizard monkey moose mouse otter owl panda python rabbit rat shark sheep
    skunk squid tiger turkey turtle weasel whale wolf wombat zebra
    '''.split()
}

def getRandomWord(word_dict):
    # function returns a random string and its key from passed in dictionary randomly
    word_key = random.choice(list(word_dict.keys()))

    # randomly select a word from the key's list in dictionary
    word_index = random.randint(0, len(word_dict[word_key]) - 1)
    return [word_dict[word_key][word_index], word_key]

def displayBoard(missed_letters, correct_letters, secret_word):
    # function replaces blank letters with correctly guessed letters
    # and shows secret word with spaces in between each letter
    print(hangman_pics[len(missed_letters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missed_letters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secret_word)

    for i in range(len(secret_word)):
        if secret_word[i] in correct_letters:
            blanks = blanks[:i] + secret_word[i] + blanks[i+1:]

    for letter in blanks:
        print(letter, end=' ')
    print()

def getGuess(already_guessed):
    # makes sure the player only enters only 1 letter at a time
    # gives another guess if the letter was already guessed
    # returns the letter that was guessed
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in already_guessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess

def playAgain():
    # returns True if player wants to play again
    # false if otherwise
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')

# for choosing the game's difficulty
difficulty = ''
while difficulty == '':
    print('''
    Choose difficulty:
    E - Easy (8 guesses)
    M - Medium (6 guesses)
    H - Hard (4 guesses)
    If no difficulty is no difficulty is chosen,
    then difficulty will be set on E - Easy.
    ''')
    difficulty = input().upper()
    if difficulty == 'M':
        print('You have chosen M - Medium (6 guesses)')
        del hangman_pics[8]
        del hangman_pics[7]
    if difficulty == 'H':
        print('You have chosen H- Hard (4 guesses)')
        del hangman_pics[8]
        del hangman_pics[7]
        del hangman_pics[5]
        del hangman_pics[3]
    else:
        print('You have chosen E - Easy (8 guesses)')

missed_letters = ''
correct_letters = ''
secret_word, secret_set = getRandomWord(words)
game_is_done = False

# game start
while True:
    print('The secret word is in the {} category.'.format(secret_set))
    displayBoard(missed_letters, correct_letters, secret_word)

    # player's letter guess
    guess = getGuess(missed_letters + correct_letters)

    if guess in secret_word:
        correct_letters = correct_letters + guess

        # check if player successfully guessed the secret word
        found_all_letters = True
        for i in range(len(secret_word)):
            if secret_word[i] not in correct_letters:
                found_all_letters = False
                break

        if found_all_letters:
            print('Yes! The secret word is "{}"! You have won!'.format(secret_word))
            game_is_done = True
    else:
        missed_letters = missed_letters + guess

        # check if player ran out of guesses
        if len(missed_letters) == len(hangman_pics) - 1:
            displayBoard(missed_letters, correct_letters, secret_word)
            print(
                '''
                You have run out of guesses!
                After {} missed guesses and {} correct guesses, the word was "{}".
                '''.format(str(len(missed_letters)), str(len(correct_letters)), secret_word))
            game_is_done = True

    # asks if player wants to play again
    if game_is_done:
        if playAgain():
            missed_letters = ''
            correct_letters = ''
            game_is_done = False
            secret_word, secret_set = getRandomWord(words)
        else:
            print("Thank you for playing!")
            break