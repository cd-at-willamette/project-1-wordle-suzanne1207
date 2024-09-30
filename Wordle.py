########################################
# Name: Suzanne Gunderson
# Collaborators (if any): QUAD Center Tutoring for some milestones
# OpenAI Transcript (if any): N/A
# Estimated time spent (hr): 8
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    correct = "" # starting word is empty
    while len(correct) != 5: # while the starting word isn't 5 letters long, we need to generate a new one.
        randomword = random.choice(ENGLISH_WORDS) # generates a random word from ENGLISH_WORDS
        if len(randomword) == 5: # checks to make sure the word is 5 letters long
            correct = randomword.upper() # if 5 letters long, reassigns new word as the random word
    print(correct) # prints the correct word

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")

        rownumber = gw.get_current_row() # finds what row you're on
        string = "" # sets the string as empty so you can add onto it
        for i in range(N_COLS):
            letter = gw.get_square_letter(rownumber,i)
            string += letter # adds the letter to the string
        is_english_word(string)
        if is_english_word(string) and len(string) == 5: # checks to make sure the guess is an english word and five letters long
            gw.show_message(string)
        else:
            #for i in range(len(string)):
             #   gw.set_key_color(string[i], "white")
            gw.show_message("Not in word list, choose another word.") # asks player to choose another word because it's either too short or not english
            rownumber = rownumber - 1 # stays on current row so player can still have enough guesses
        color_row(string, correct)
        greensquare = 0
        for i in range(5):
            if gw.get_square_color(rownumber, i) == "green":
                greensquare = greensquare + 1
                print(greensquare)
        if greensquare == 5: # checks to see if an entire row is green
            gw.show_message("Congrats, you won!")
        else:
            if rownumber == 5: # checks to see if the player has reached the end of the game without a correct guess
                gw.show_message("Nice try. The word was " + correct)
            else:
                gw.set_current_row(rownumber + 1) # moves to the next row
        for i in range(len(string)): # looks at each letter in the guessed word
            letter = string[i] # assigns letter variable
            if len(string) == 5:
                if gw.get_square_color(rownumber, i) == "green": # checks to see if the guess was correct
                    gw.set_key_color(letter, "green") # turns key color green
                if gw.get_key_color(string[i]) != "green": # checks to make sure the green keys stay green no matter if you make another guess with the letters in the wrong spot
                    if gw.get_square_color(rownumber, i) == "yellow": # checks to see if the guess is in the word
                        gw.set_key_color(letter, "yellow") # turns key color yellow
                    if gw.get_square_color(rownumber, i) == "grey": # checks to see if the guess letter is not in the word
                        gw.set_key_color(letter, "grey")
            

    def color_row(guess, correct):
        if len(guess) < 5:
            print("meow")
            #for i in range(len(guess)):
                #gw.set_key_color(guess[i], "white")
        else:
            letters_left = correct # at the start, the letters left is just the word
            rownumber = gw.get_current_row() # sets variable to current row
            print(guess)
            print(correct)
            for i in range(len(guess)): # goes through each letter in the guessed word
                if guess[i] == correct[i]: # if the letter in the guess is the same as the letter in the correct word
                    gw.set_square_color(rownumber, i, "green") # sets square color to green
                    print("green")
                    letters_left = remove_letter(letters_left, guess[i]) # removes the letter from the letters left list so python doesn't keep looping
                    print(letters_left)
            for i in range(len(guess)):
                if gw.get_square_color(rownumber, i) != "green": # checks to make sure you don't recolor the green squares
                    if guess[i] in letters_left: # if the letter is in the word
                        gw.set_square_color(rownumber, i, "yellow") # set square to yellow
                        letters_left = remove_letter(letters_left, guess[i]) # removes the yellow letter from the letters left list
                        print(letters_left) # prints the new letters left list
                    else:
                        gw.set_square_color(rownumber, i, "grey") # simply colors the square grey because not in word

    def remove_letter(word, letter):
        word = word.replace(letter, "", 1) # replaces ith letter with an empty space 1 time
        return word # returns the new string without the letter already guesed
    

            


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    #word = "sassy"
    # correct = "glass"
    #gw.set_square_letter(0,0,word[0]) # Takes the 0th row, 0th column, and the 0th letter from our word.
    #gw.set_square_letter(0,1,word[1])
    #gw.set_square_letter(0,2,word[2])
    #gw.set_square_letter(0,3,word[3])
    #gw.set_square_letter(0,4,word[4])

    



# Startup boilerplate
if __name__ == "__main__":
    wordle()
