from os import system, name
from random import randint, random

words = ["beekeeper", "groundhog", "graveyard", "software"]
num_of_words = len(words)

random_word_selection = randint(0, num_of_words-1)
word_to_guess = words[random_word_selection]

guessed_answer = []

for dash in range(0,len(word_to_guess)):
    guessed_answer.append("_")
    
for i in guessed_answer:
    print(i, end = ' ')

print("\n")

lives = 3
word_found = False
num_of_blanks = len(word_to_guess)
while(lives!=0):
    system('clear')
    print(f"You only have {lives} left\n")
    for i in guessed_answer:
        print(i, end = ' ')
    print("\n")
    selected_letter = input("Select your letter: ")
    
    for i in range(0,len(word_to_guess)):
        if(selected_letter == word_to_guess[i]):
            guessed_answer[i] = selected_letter
            word_found = True
            
    if(word_found == False):
        lives-=1
    word_found = False

    for i in guessed_answer:
        if(i != "_"):
            num_of_blanks-=1
    
    if(num_of_blanks == 0):
        print(f"You have won!\nWord was {word_to_guess}")
        break

    if(lives == 0):
        print("Game over")
    num_of_blanks = len(word_to_guess)
