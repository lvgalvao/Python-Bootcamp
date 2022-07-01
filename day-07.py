#Step 1 
from random import randint, random

word_list = ["aardvark", "baboon", "camel"]

#Todo-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.

chosen_word = word_list[randint(0, len(word_list)-1)]
print(chosen_word)

#Todo-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.

guess = input("Guess a letter ").lower()
print(guess)

#Todo-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.

# result = chosen_word.find(guess)
# print(result)

for letter in chosen_word:
    if letter == guess:
        print("Right")
    else:
        print("wrong")