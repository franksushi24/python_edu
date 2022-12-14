# GAME LOOP

import random
import time

# A WHILE LOOP LETS US LOOP AS MANY TIMES AS IT TAKES WHERE IT IS UNDEFINED 
print("Hi! Welcome to the guess game. I am going to pick a number between 1 and 100.")
time.sleep(3)
print("Picking a number...")
time.sleep(2)
guess = int(input("What is your guess?: "))
correct_number = random.randint(1,100)
guess_count = 1

while guess != correct_number:
    time.sleep(1)
    guess_count += 1
    if guess < correct_number:
        guess = int(input("Wrong. You need to guess higher. What is your new guess?: "))
    else: guess = int(input("Wrong. You need to guess lower. What is your new guess?: "))
     

print(f"Congrats! The right answer was {correct_number}. It took you {guess_count} guesses!")
