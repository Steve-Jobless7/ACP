import random

# Function to play the number guessing game
def number_guessing_game():
    # Generate a set of random numbers between 1 and 100 (5 unique numbers)
    numbers_to_guess = set(random.sample(range(1, 101), 5))  # 5 random numbers between 1 and 100
    
    # Create a dictionary to store guesses and their corresponding feedback
    guess_feedback = {}
    
    # Create a list to store guesses (for record keeping)
    guesses = []
    
    print("Welcome to the Number Guessing Game!")
    print(f"I have selected {len(numbers_to_guess)} different numbers between 1 and 100.")
    print("Try to guess one of them!")

    # Loop to keep asking the player to guess until they get it right
    while True:
        # Prompt the user to enter their guess
        guess = input(f"Enter your guess (between 1 and 100): ")
        
        # Validate input: ensure the input is a number and within the range 1-100
        if not guess.isdigit() or not (1 <= int(guess) <= 100):
            print("Please enter a valid number between 1 and 100!")
            continue
        
        # Convert the guess to an integer
        guess = int(guess)
        
        # Add the guess to the list of guesses for record keeping
        guesses.append(guess)
        
        # Store feedback for the guess in the dictionary
        if guess in numbers_to_guess:
            guess_feedback[guess] = 'correct'
            print(f"Congratulations! {guess} is one of the correct numbers.")
            print(f"It took you {len(guesses)} guesses.")
            break
        else:
            # Provide feedback whether the guess is too high or too low
            if guess < min(numbers_to_guess):
                guess_feedback[guess] = 'too low'
                print("Your guess is too low. Try again!")
            elif guess > max(numbers_to_guess):
                guess_feedback[guess] = 'too high'
                print("Your guess is too high. Try again!")
            else:
                guess_feedback[guess] = 'incorrect'
                print("Your guess is incorrect. Try again!")

    # Print the list of guesses and their feedback
    print(f"\nYour guesses and their feedback:")
    for guess in guesses:
        feedback = guess_feedback[guess]
        if feedback == 'too low':
            print(f"Guess: {guess}, Feedback: Your guess is too low.")
        elif feedback == 'too high':
            print(f"Guess: {guess}, Feedback: Your guess is too high.")
        elif feedback == 'correct':
            print(f"Guess: {guess}, Feedback: Congratulations, that’s correct!")

# Main function to run the game
if __name__ == "__main__":
    number_guessing_game()