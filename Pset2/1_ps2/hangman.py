# Problem Set 2, hangman.py
# Name: Juan Rached
# Collaborators: Nelson Hidalgo
# Time spent: 6 hours

import random
import string

# -----------------------------------
# HELPER CODE
# -----------------------------------

WORDLIST_FILENAME = "words.txt"

def load_words():
    """
    returns: list, a list of valid words. Words are strings of lowercase letters.    
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print("Loading word list from file...")
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r')
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = line.split()
    #print("  ", len(wordlist), "words loaded.")
    return wordlist

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)
    
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def help_reveal(secret_word, available_letters):
    
    #Creates a  string that contains letters that are available and in the secret word
    choose_from = ""
    for letter in set(secret_word):
        if letter in available_letters:  
            choose_from = choose_from + letter

    #Chooses a random letter from string
    new = random.randint(0, len(choose_from)-1) 
    revealed_letter = choose_from[new]
    
    return revealed_letter 

def score(secret_word, counter):
    
    abc = string.ascii_lowercase
    unique = 0
    
    #Finds number of unique letters
    for i in range(len(abc)):
        if abc[i] in secret_word:
            unique = unique + 1
        
    #returns player score
    return 2*unique*counter + 3*len(secret_word)

# -----------------------------------
# END OF HELPER CODE
# -----------------------------------


# Load the list of words to be accessed from anywhere in the program
wordlist = load_words()
secret_word = choose_word(wordlist)

def has_player_won(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: boolean, True if all the letters of secret_word are in letters_guessed,
        False otherwise
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    previous = True
    
    for i in range(len(secret_word)):
        right = False 
        if secret_word[i] in letters_guessed:
               right = True
        previous = previous and right
        
    return previous


def get_word_progress(secret_word, letters_guessed):
    '''
    secret_word: string, the lowercase word the user is guessing
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters and asterisks (*) that represents
        which letters in secret_word have not been guessed so far
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    progress = ""
    
    for i in range(len(secret_word)): 
        if secret_word[i] in letters_guessed:
            reveal = secret_word[i]
        else:
            reveal = "*"
        progress += reveal
            
    return progress
    


def get_available_letters(letters_guessed):
    '''
    letters_guessed: list (of lowercase letters), the letters that have been
        guessed so far

    returns: string, comprised of letters that represents which
      letters have not yet been guessed. The letters should be returned in
      alphabetical order
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    
    counter = 0 #counter of available letters
    available_letters = string.ascii_lowercase
    for letter in available_letters:
        if letter in letters_guessed or letter.upper() in  letters_guessed:
            if counter == 0: #conditional to avoid errors in splicing for ind=0
                available_letters = '' + available_letters[1:] 
                counter = counter - 1
            else:
                available_letters = available_letters[:counter] + '' + available_letters[counter + 1:]
                #^slices string to take out the letter already guessed
                counter = counter - 1 #Since the string loss one letter, take the counter back by 1
        counter = counter + 1
    
    return available_letters
    
    

def hangman(secret_word, with_help):
    '''
    secret_word: string, the secret word to guess.
    with_help: boolean, this enables help functionality if true.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many
      letters the secret_word contains and how many guesses they start with.

    * The user should start with 10 guesses.

    * Before each round, you should display to the user how many guesses
      they have left and the letters that the user has not yet guessed.

    * Ask the user to supply one guess per round. Remember to make
      sure that the user puts in a single letter (or help character '^'
      for with_help functionality)

    * If the user inputs an incorrect consonant, then the user loses ONE guess,
      while if the user inputs an incorrect vowel (a, e, i, o, u),
      then the user loses TWO guesses.

    * The user should receive feedback immediately after each guess
      about whether their guess appears in the computer's word.

    * After each guess, you should display to the user the
      partially guessed word so far.

    -----------------------------------
    with_help functionality
    -----------------------------------
    * If the guess is the symbol ^, you should reveal to the user one of the
      letters missing from the word at the cost of 3 guesses. If the user does
      not have 3 guesses remaining, print a warning message. Otherwise, add
      this letter to their guessed word and continue playing normally.

    Follows the other limitations detailed in the problem write-up.
    '''
    # FILL IN YOUR CODE HERE AND DELETE "pass"
    letters_guessed = [] #Empty list where letters guessed will go
    counter = 10 #Start with ten guesses
    
    print("Welcome to hangman!\nI am thinking of a " + str(len(secret_word)) + " letter word.") 
    
    #Main loop. Runs as long as player has not won or run out of guesses
    while counter > 0 and has_player_won(secret_word, letters_guessed) == False :
        #Displays number of guesses left and available letters. Asks user for letter input
        print("-----------------")
        print("You have " + str(counter) + " guesses left")
        print("Available letters: "+ get_available_letters(letters_guessed))
        guess = input("Please guess a letter: ").lower()
        
        #For any input that is not "^" or a letter, you can only enter it once.
        if guess != "^":
            if guess in letters_guessed:
                print("Oops! You have already guessed that letter: " + get_word_progress(secret_word, letters_guessed))
                continue
            
        #Add guesses to guessed list
        letters_guessed.append(guess)
        
       
        #Makes sure inputs is only one letter
        if guess.isalpha() == True and len(guess) < 2:
            if guess in secret_word:
                print("Good guess: " + get_word_progress(secret_word, letters_guessed))
            else:
                #For vowels take two guess
                if guess == "a" or guess == "e"  or guess == "i"  or guess == "o"  or guess == "u":     
                    counter = counter -2
                    print("Oops! That letter is not on my word: " + get_word_progress(secret_word, letters_guessed))
                else:
                    counter = counter -1
                    print("Oops! That letter is not on my word: " + get_word_progress(secret_word, letters_guessed))  
        #If we are playing with help.
        elif guess == "^" and with_help == True: 
            if counter < 3:#If you have less than three guesses you can't use help
                print('Ooops! Not enough guesses left: ', get_word_progress(secret_word, letters_guessed))
            else:
                #reduces three guesses every time help is used
                counter = counter - 3
                guess = help_reveal(secret_word, get_available_letters(letters_guessed)) 
                print("Letter revealed: ", guess)
                letters_guessed.append(guess)
                print(get_word_progress(secret_word, letters_guessed))
        else:
                print("Oops! That is not a valid letter. Please input a letter from the alphabet: " + get_word_progress(secret_word, letters_guessed))
            
                        

#Winning message              
    if has_player_won(secret_word, letters_guessed) == True:
        print("-----------------")
        print("Congratulations, you won!\nYour total score for this game is: ", score(secret_word, counter))
    #loosing message
    else:
        print("-----------------")
        print("Sorry, you ran out of guesses. The word was: " + secret_word)
        

# When you've completed your hangman function, scroll down to the bottom
# of the file and uncomment the lines to test

if __name__ == "__main__":
    # To test your game, uncomment the following two lines.
    #    secret_word = choose_word(wordlist)
    with_help = True
    hangman(secret_word, with_help)

    # After you complete with_help functionality, change with_help to True
    # and try entering "^" as a guess!

    ###############

    # SUBMISSION INSTRUCTIONS
    # -----------------------
    # It doesn't matter if the lines above are commented in or not
    # when you submit your pset. However, please run ps2_student_tester.py
    # one more time before submitting to make sure all the tests pass.
    pass