# HANGMAN in PYTHON

# uložen word list in (words.py)

import random  # zpřístupní fce modulů s výběrem náhodných prvků ze seznamu
from words import word_list #list of random words


def get_word(): # fce get word
    return random.choice(word_list).upper()
    # lowercase letters in uppercase


# Hangman drawing ... stages that are based on incorrect guessed letters by player
hangman_art = {
               0: ("   ",
                   "   ",
                   "   ",), # 3 incorrect guesses - no hangman on display we can´t see our hangman person....
               1: (" o  ",
                   "    ",
                   "    ",), # 1 incorrect guess we will display head
               2: (" o  ",
                   " |  ",
                   "    ",), # 2 incorrect guesses we will display main corpse of body
               3: (" o  ",
                   "/|  ",
                   "    " ,), # 3 incorrect guesses we will display left arm
               4: (" o  ",
                   "/|\\", # 4 incorrect guesses we will display right arm
                   "/   ",),
               5: (" o  ",
                   "/|\\",
                   "/   ",), # 5 incorrect guesses we will display left leg
               6: (" o  ",
                   "/|\\",
                   "/ \\",)
}

# now we try if it works:
# for line in hangman_art[0]:
#    print(line) # for 0 guesses will not display a hangman
#for line in hangman_art[3]:
#  print(line) # 3 incorrect guesses will display hangman (head, body and left hand)

def display_man(wrong_guesses): #fce display man
    #pass
    print("**********")
    if wrong_guesses <= 3:
        hangman_state = 0
    else:
        hangman_state = wrong_guesses - 3

    for line in hangman_art[hangman_state]: #will draw part of hangman by wrong guesses
        print(line) # test run: Enter a letter
    print("**********")


def display_hint(hint): #fce display hint
    #pass
    print(" ".join(hint)) # now test run will display hangman with Enter a letter and underscore to represent each character and each separated with a space:

#def display_answer(answer):
#pass
#   print(" ".join(answer)) will display correct answer when game ends.....


def main(): #fce shows the logic of the game
    answer = get_word() # choose random word
    hint = ["-"] * len(answer) #if we guess wrong letter it will count them
    wrong_guesses = 0 # changing number will display hangman by the wrong guesses...with 6 wrong guesses we loose
    guessed_letters = set() # set of guessed letters

    while True: #game loop
        display_man(wrong_guesses) #shows actual status og game
        display_hint(hint) #this one as well

        guess = input("Enter a letter: ").upper() #player will enter the game ....writing a letter


        if len(guess) == 1 and guess.isalpha(): # single letter guess
            if guess in guessed_letters:
                print(f"{guess} has already been guessed.")  # will show already guessed characters
                continue


            guessed_letters.add(guess)


            if guess in answer: # Correct letter
                for i in range(len(answer)):
                     if answer[i] == guess:
                         hint [i] = guess


            else:
                wrong_guesses += 1
                print(f"{guess}is not in the word. ")


        elif len(guess) == len(answer) and guess.isalpha():# full word guess
            if guess == answer:
                hint = list(answer) #will update hint to display a full word
                print("YOU WIN")
                break
            else:
                print(f"{guess} is not correct word. ")
                wrong_guesses += 1


        else:
            print("Invalid input. Please enter a single letter. ")
            continue


        # Win condition..if there is no "_" player win
        if "-" not in hint:
            display_man(wrong_guesses)
            display_hint(hint)
            print("YOU WIN!")
            break



        # Lose condition....if counting of wrong letters will get to 6 player lose
        if wrong_guesses >= 9:
            display_man(wrong_guesses)
            print("YOU LOSE! The word was:", answer)
            break


if __name__ == "__main__":
   main()
