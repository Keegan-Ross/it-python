import random
from banner import banner

banner("ROCK, PAPER, SCISSORS", "Keegan Ross")
print("We are going to play a game of Rock, Paper, Scissors. The first to win two times out of 3 rounds is the winner.")

cpu_score = 0
player_score = 0
while player_score < 2 and cpu_score < 2:
    print(f"SCORE: Player: {player_score} Computer: {cpu_score}")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    players_choice = int(input("What is your choice? "))
    cpu_choice = random.randint(1,3)
    if players_choice == 1:
        if cpu_choice == 1:
            print("Tie")
        if cpu_choice == 2:
            print("Lose")
            cpu_score += 1
        if cpu_choice == 3:
            print("Win")
            player_score += 1
    if players_choice == 2:
        if cpu_choice == 1:
            print("Win")
        if cpu_choice == 2:
            print("Tie")
            cpu_score += 1
        if cpu_choice == 3:
            print("Lose")
            player_score += 1
    if players_choice == 3:
        if cpu_choice == 1:
            print("Lose")
        if cpu_choice == 2:
            print("Win")
            cpu_score += 1
        if cpu_choice == 3:
            print("Tie")
            player_score += 1

    if player_score == 2:
        print("Congratulations you have defeated the computer! Your robotic overlords tremble in fear!")
    if cpu_score ==2:
        print("Sorry for your loss, but the computer reigns superior!")




