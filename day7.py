
import random

notwords = 'ant babboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk lion lizard llama mole rat raven rhino shark sheep spider toad turkey turtle wolf wombat zebra'

words_list = notwords.split()

def get_word():
    word = random.choice(words_list)
    return word

HANGMAN_PICS = ["""
  +--+
  |  |
     |
     |
     |
     |
 =====""",


 """
  +--+
  |  |
  O  |
     |
     |
     |
 =====""",


 """
  +--+
  |  |
  O  |
  |  |
     |
     |
 =====""",


 """
  +--+
  |  |
  O  |
 /|  |
     |
     |
 =====""",


 """
  +--+
  |  |
  O  |
 /|\ |
     |
     |
 =====""",


 """
  +--+
  |  |
  O  |
 /|\ |
 /   |
     |
 =====""",

 
 """
  +--+
  |  |
  O  |
 /|\ |
 /|\ |
     |
 ====="""]

print(HANGMAN_PICS[6])



print("Welcome to Hangman Game")

word = get_word()
display = []    

for i in range(len(word)):
    display += "_"

print(display)


def hangman():
    chances = 0
    while chances < 6:
        guess = input("Guess a letter: ")
        if len(guess) > 1:
            print("Please enter a single letter")
            continue
        if guess in word:
            for i in range(len(word)):
                if word[i] == guess:
                    display[i] = guess
            print(display)
        else:
            chances += 1
            print(HANGMAN_PICS[chances])
            if (chances==6):
                print(f"You lose the word was {word}")
                break
        if "_" not in display:
            print("You win")
            break
    

hangman()


