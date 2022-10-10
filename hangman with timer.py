import random
import string
from words import words  # This imports the list of words from the words module.
import time


def get_valid_word():
    word = random.choice(words)  # this randomly selects a word from the words list that was imported and stores it
    # the stated variable

    while '-' in word or ' ' in word:
        word = random.choice(words)

    return word.upper()


def hangman():
    word = get_valid_word()
    word_letters = set(word)  # sets the individual letters in the word
    alphabet = set(string.ascii_uppercase)  # sets all the letters in the English language
    used_letters = set()

    lives = 7
    timeout = len(word) * 10
    timeout_start = time.time()

    print("YOU HAVE " + str(timeout) + " SECONDS TO PLAY THIS GAME!")

    while len(word_letters) > 0 and lives > 0 and time.time() < timeout_start + timeout:

        if lives > 1:
            print('you have ' + str(lives) + ' lives left and you have used these letters: ', ' '.join(used_letters))
        elif lives == 1:
            print('you have ' + str(lives) + ' life left and you have used these letters: ', ' '.join(used_letters))

        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ', ''.join(word_list))

        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet and user_letter not in used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
                #print('')

            else:
                lives = lives - 1
                print('letter is not in word')

        elif user_letter in used_letters:
            print('you have already used that character. Please try again')
            print(timeout)
        else:
            print('invalid character. Please try again')

    if lives == 0:
        print('sorry, you died. The word was ' + word)
    elif len(word_letters) == 0:
        print('You guessed the word ' + word + '!')
    else:
        print("sorry, you ran out of time!, the word was " + word)


hangman()


def play_again():

    replay = input("play again? (Y/N)").lower()
    if replay == 'y':
        hangman()
    elif replay == 'n':
        print('thanks for playing')
    else:
        play_again()


play_again()
