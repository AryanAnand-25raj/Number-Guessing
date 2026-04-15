"""
    Improved simple number guessing game
    Added difficulty levels and scoring system.
"""
import random

def get_difficulty():
    while True:
        print("\nChoose difficulty level:")
        print("1. Easy   (Range: 1-50, Attempts: 10)")
        print("2. Medium (Range: 1-100, Attempts: 7)")
        print("3. Hard   (Range: 1-200, Attempts: 5)")
        choice = input("Enter your choice (1/2/3): ").strip()
        
        if choice == '1':
            return 50, 10, "Easy"
        elif choice == '2':
            return 100, 7, "Medium"
        elif choice == '3':
            return 200, 5, "Hard"
        else:
            print("Invalid choice! Please select 1, 2, or 3.")

def calculate_score(attempts_left, max_attempts, difficulty_multiplier):
    # Base score depends on speed (attempts left) and difficulty
    # More attempts left = higher score
    # Higher difficulty = higher multiplier
    return (attempts_left + 1) * 10 * difficulty_multiplier

def play_game():
    print("Welcome to the Improved Number Guessing Game!")
    
    max_range, max_attempts, diff_name = get_difficulty()
    secret_number = random.randint(1, max_range)
    attempts = max_attempts
    is_guess_correct = False
    
    # Difficulty multiplier for scoring
    multiplier = {"Easy": 1, "Medium": 2, "Hard": 5}[diff_name]
    
    print(f"\nYou selected {diff_name} mode.")
    print(f"The secret number lies between 1-{max_range}.")
    
    while attempts > 0:
        print(f"\nYou have {attempts} attempts remaining.")
        try:
            user_input = input("Enter your guess: ").strip()
            if not user_input:
                continue
            user_number = int(user_input)
        except ValueError:
            print("Please enter a valid number.")
            continue
        
        if user_number == secret_number:
            print("Congrats! Your guess is right!")
            is_guess_correct = True
            
            # Scoring: more points for fewer attempts and higher difficulty
            score = calculate_score(attempts - 1, max_attempts, multiplier)
            print(f"Your Score: {score}")
            break
        else:
            if user_number < secret_number:
                print("Your guess is wrong! Try a HIGHER number.")
            else:
                print("Your guess is wrong! Try a LOWER number.")
        
        attempts -= 1

    if not is_guess_correct:
        print("\nBad Luck!! You couldn't guess the number.")
        print(f"Your final score: 0")

    print(f"The secret number was {secret_number}.")
    print("Game Over!")

if __name__ == "__main__":
    play_game()
