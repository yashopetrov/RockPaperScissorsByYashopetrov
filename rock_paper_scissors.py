from random import randint

rock = "Rock"
paper = "Paper"
scissors = "Scissors"
computer_move = ""
play_game = True
win_count = 0
lost_count = 0
draw_count = 0

while play_game:
    player_move = input("Choose Rock[r], Paper[p] or Scissors[s]: ").lower()

    if player_move == "r":
        player_move = rock
    elif player_move == "p":
        player_move = paper
    elif player_move == "s":
        player_move = scissors
    else:
        raise SystemExit("Invalid Input. Try again...")

    random_number = randint(1, 3)

    if random_number == 1:
        computer_move = rock
    elif random_number == 2:
        computer_move = paper
    else:
        computer_move = scissors

    print(f"You chose {player_move}")
    print(f"Computer chose {computer_move}")

    # First case - Player wins
    if (player_move == rock and computer_move == scissors) or \
            (player_move == paper and computer_move == rock) or \
            (player_move == scissors and computer_move == paper):
        win_count += 1
        print("You win! :) \n")
    elif player_move == computer_move:
        draw_count += 1
        print("Draw! :| \n")
    else:
        lost_count += 1
        print("You lose! :( \n")

    new_game = input("One more game? (Y): ").lower()  # Ask the player for a new game.

    if new_game == "y":  # Continue the game if player agrees.
        continue
    else:  # Show total results and exit game if player doesn't agree.
        print(f"Final score: {win_count} wins, {lost_count} losses and {draw_count} draws.")
        print("See you next time. Bye! :)")
        play_game = False
        break
