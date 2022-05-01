#December 20,2021
#This program allows the user to play hangman with the computer. 




import random
from words import words

def get_valid_word(words):
    word = random.choice(words) #randomly chooses something from list
    while '-' in word or '' in word:
        word = random.choice(words)

    return word

def main():
    word = get_valid_word(words)
    word_letters = set(word) #letters in the word
    alphabet = set(string.ascii_uppercase)
    used_letters = set() #what the ser has guessed

    #number of lives
    lives = 5

    
    #getting user input
    while len(word_letters)>0:
        #letters usedd
        #''.join(['a','b','cd'])---> 'a b cd'
        print('You have',lives,'lives left and used these letters:', ''.join(used_letters))



        #what current word is (ie W - R D)
        word_list = [letter if letter in used_letters else '-' for letter in word]
        print('Current word: ',''.join(word_list))
        
         
        user_letter = input('Guess a letter: ').upper()
        if user_letter in alphabet - used_letters:
            used_letters.add(user_letter)
            if user_letter in word_letters:
                word_letters.remove(user_letter)
            else:
                lives = lives - 1
                print('Letter is not in word.')

        elif user_letter in user_letters:
            print('You already used that chracter.Please try again.')

        else:
            print('Invalid character. Please try again.')
        
    #gets here when len(word_letters) == 0 OR when lives == 0
    if lives == 0:
        print('You died, sorry. The word was',word)

    else:
        print('You guessed the word', word,'!!')

