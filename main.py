import random

# Game choices
snake = 1
water = 2
gun = 3

# Initialize scores
player_score = 0 
computer_score = 0

# Keep playing until the user chooses to quit
while True:
        # Take the player's choice
        choice = int(input("Enter your choice (1 = Snake, 2 = Water, 3 = Gun): "))
        if choice < 1 or choice > 3:
            print("invalid choice!")
            continue

        # Generate a random choice for the computer
        computer = random.randint(1,3)
        print("Computer choice:", computer)

        # Display the player's selected choice
        if (choice == snake):
            print("you chose snake")
        elif (choice == water):
            print("you chose water")
        elif (choice == gun):
            print("you chose gun")


        # Check whether the round is a draw
        if (choice == computer):
            print("It's a draw!")
        else:
            if (choice == snake and computer == water):
                print("You win!")
                player_score += 1
            elif(choice == snake and computer == gun):
                print("You lose!")
                computer_score += 1
            elif(choice == water and computer == snake):
                print("You lose!")
                computer_score += 1
            elif(choice == water and computer == gun):
                print("You win!")
                player_score += 1
            elif(choice == gun and computer == snake):
                print("You win!")
                player_score += 1
            elif(choice == gun and computer == water):
                print("You lose!")
                computer_score += 1


        # Display the current scores
        print("player score:", player_score)
        print("computer score:", computer_score)
 
         # Ask whether the player wants another round
        play_again = input("Do you want to play again? (y/n): ")

        # Exit the loop if the player chooses no
        if play_again == "n":
            break
   
    