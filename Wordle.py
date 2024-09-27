########################################
# Name: Suzanne Gunderson
# Collaborators (if any): QUAD Center Tutoring
# OpenAI Transcript (if any): N/A
# Estimated time spent (hr):
# Description of any added extensions:
########################################

from WordleGraphics import *  # WordleGWindow, N_ROWS, N_COLS, CORRECT_COLOR, PRESENT_COLOR, MISSING_COLOR, UNKNOWN_COLOR
from english import * # ENGLISH_WORDS, is_english_word
import random

def wordle():
    # The main function to play the Wordle game.
    correct = ""
    while len(correct) != 5:
        randomword = random.choice(ENGLISH_WORDS)
        if len(randomword) == 5:
            correct = randomword
    print(correct)

    def enter_action():
        # What should happen when RETURN/ENTER is pressed.
        gw.show_message("You need to implement this method")

        rownumber = gw.get_current_row()
        string = ""
        for i in range(N_COLS):
            letter = gw.get_square_letter(rownumber,i)
            string += letter
        is_english_word(string)
        if is_english_word(string) and len(string) == 5:
            gw.show_message("Good choice!")
        else:
            gw.show_message("Not in word list.")
        color_row(word, correct)

    def color_row(guess, correct):
        letters_left = correct
        rownumber = gw.get_current_row()
        for i in range(len(guess)):
            if guess[i] == correct[i]:
                gw.set_square_color(rownumber, i, "green")
                letters_left = remove_letter(letters_left, guess[i])
                print(letters_left)
        for i in range(len(guess)):
            if gw.get_square_color(rownumber, i) != "green":
                if guess[i] in letters_left:
                    gw.set_square_color(rownumber, i, "yellow")
                    letters_left = remove_letter(letters_left, guess[i])
                    print(letters_left)
                else:
                    gw.set_square_color(rownumber, i, "grey")

    def remove_letter(word, letter):
        word = word.replace(letter, "", 1)
        return word
    

            


    gw = WordleGWindow()
    gw.add_enter_listener(enter_action)
    word = "sassy"
    # correct = "glass"
    gw.set_square_letter(0,0,word[0]) # Takes the 0th row, 0th column, and the 0th letter from our word.
    gw.set_square_letter(0,1,word[1])
    gw.set_square_letter(0,2,word[2])
    gw.set_square_letter(0,3,word[3])
    gw.set_square_letter(0,4,word[4])

    



# Startup boilerplate
if __name__ == "__main__":
    wordle()
