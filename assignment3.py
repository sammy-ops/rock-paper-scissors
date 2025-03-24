import random

# Function to display welcome message
def welcome():
    print("\nWelcome to Rock, Paper, Scissors!")
    print("Rules: Rock beats Scissors, Scissors beats Paper, Paper beats Rock.\n")

# Function to get the computer’s choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner
def determine_winner(player, computer):
    if player == computer:
        return "draw"
    elif (player == "rock" and computer == "scissors") or \
         (player == "scissors" and computer == "paper") or \
         (player == "paper" and computer == "rock"):
        return "player"
    else:
        return "computer"

# Function to play the game
def play_game():
    scores = {"player": 0, "computer": 0}
    
    for round_num in range(1, 4):  # Best of 3 rounds
        print(f"\nRound {round_num}")
        player_choice = input("Choose rock, paper, or scissors: ").strip().lower()

        if player_choice not in ["rock", "paper", "scissors"]:
            print("Invalid choice! Try again.")
            play_game()
        
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")

        winner = determine_winner(player_choice, computer_choice)
        if winner == "Player":
            print("You win this round!")
            scores["player"] += 1
        elif winner == "computer":
            print("Computer wins this round!")
            scores["computer"] += 1
        else:
            print("🤝 It's a draw!")

    # Final results
    print("\n🏆 Final Scores:")
    print(f"🔹 You: {scores['player']} | 🤖 Computer: {scores['computer']}")

    if scores["player"] > scores["computer"]:
        print("🎉 Congratulations! You won the game! 🏅")
    elif scores["player"] < scores["computer"]:
        print("😔 Better luck next time! The computer won! 🏆")
    else:
        print("🤝 It's a tie! Well played!")

# Main function
def main():
    welcome()
    while True:
        play_game()
        play_again = input("\n🔄 Play again? (yes/no): ").strip().lower()
        if play_again != "yes":
            print("👋 Thanks for playing! Goodbye!\n")
            break

if __name__ == "__main__":
    main()
