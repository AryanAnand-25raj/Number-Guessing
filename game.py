"""
    Create a simple number guessing game
    The user gets 10 chances to guess a number
"""
import random

print("Welcome to the number guessing game {All-The-Best}!")
print("The Secret number lies between 1-50")
secret_number = random.randint(1, 50)
attempts = 10
is_guess_correct = False

while attempts > 0:
    print(f"\nYou have {attempts} attempts remaining.")
    user_number = int(input("Enter your guess: "))
    
    if user_number == secret_number:
        print("Congrats! Your guess is right!")
        is_guess_correct = True
        break
    else:
        if user_number < secret_number:
            print(f"Your guess is wrong! Try a HIGHER number.")
        else:
            print(f"Your guess is wrong! Try a LOWER number.")
    
    attempts -= 1

# This runs AFTER the loop ends
if not is_guess_correct:
    print("\nBad Luck!! You couldn't guess the number.")

print(f"The secret number was {secret_number}.")
print("Game Over!")