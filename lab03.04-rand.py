#Lab3 Exercise4, program random number between 1 and 10
import random

guess=int(input("You've a 1 in 10 chance of getting the answer right, go on guess..."))
the_chosen_num=random.randint(1,10)
if guess == the_chosen_num:
    result="CORRECT!"
else:
    result="WRONG!"
print("Drum roll please...")
print(f"You, guessed, {guess}")
print(f"And you were {result} the chosen number was {the_chosen_num}")
