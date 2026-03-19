import random

# List of choices
choices = ["snake", "water", "gun"]

# Initialize scores
user_score = 0
computer_score = 0

# Number of rounds
rounds = 5

print("Welcome to Snake-Water-Gun Game!")
print("Choices are: snake, water, gun\n")

for i in range(rounds):
    user_choice = input(f"Round {i+1} - Enter your choice: ").lower()
    if user_choice not in choices:
        print("Invalid choice! Try again.\n")
        continue

    computer_choice = random.choice(choices)
    print(f"Computer chose: {computer_choice}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!\n")
    elif (user_choice == "snake" and computer_choice == "water") or \
         (user_choice == "water" and computer_choice == "gun") or \
         (user_choice == "gun" and computer_choice == "snake"):
        print("You win this round!\n")
        user_score += 1
    else:
        print("Computer wins this round!\n")
        computer_score += 1

# Final result
print("Game Over!")
print(f"Your score: {user_score} | Computer score: {computer_score}")

if user_score > computer_score:
    print("Congratulations! You won the game 🏆")
elif user_score < computer_score:
    print("Computer won the game! 💻")
else:
    print("The game is a tie! 🤝")