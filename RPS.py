import random 

# A program that will welcome the user by entering their name
# A rock, paper, and scissor game with three (3) rounds 
# You versus the computer (Who will win?)

print("----------------------------")
print("> Press |Enter| to Continue.")
print("> Input |Q| to quit the Game")
print("> Input |T| to know the developer")
print("---------------------------------")
game = input("You v/s Computer  -- Who will win? > ").upper()
print("-------------------------")

if game == "":
    player = input("What's your name? > ").upper()
    played = player

    print("-------------------------")
    print("-----Welcome to RPS!-----")
    print("------------------------------------")
    print(f"> Hello {player} are you the chosen one? ")
    print("------------------------------------")

    RPS = ["Rock", "r", "Paper", "p", "Scissor", "s"]

    print("---" + RPS[0] + "--" + RPS[2] + "--" + RPS[4] + "--")
    print("--------------------------------")

    # Variables set to both 0
    player_score = 0
    computer_score = 0

    # While loop
    while player_score or computer_score < 3:
        player_choices = ["r", "p", "s"]
        print(f"{RPS[0]} = r  {RPS[2]} = p  {RPS[4]} = s")
        print("--------------------------------")
        computer = random.choice(player_choices)

        player = str(input("Enter your Move > ")).lower()
        print("-------------------------")
        if player == computer:
            print("> Whoa....it's a tie")
            print("--------------------------------")
    
        elif player == "r" and computer == "p" or player == "s" and computer == "r" or player == "p" and computer == "s":
            computer_score = computer_score + 1
            print(f"> Computer Won... (Round {computer_score})")
            print("-------------------------")
            print(f"Computer score is = {computer_score}")
            print("Response: Try Again Human")
            print("--------------------------------")
        if computer_score == 3:
            print("I win the game, you cannot defeat me")
            print("------------------------------------")
           
            break
        elif player == "p" and computer == "r" or player == "r" and computer == "s" or player == "s" and computer == "p":
            player_score = player_score + 1
            print(f"> You won... (Round {player_score})")
            print("-------------------------")
            print(f"Your score is = {player_score}")
            print("--------------------------------")
        if player_score == 3:
            print("You win...")
            print("-------------------------")
            break

elif game == "Q":
    print("Farewell Warrior...")
    print("-------------------------")

elif game == "T":
    # Developer information
    developer = ["Theodore Ross C. Bermejo", "1st Year", "BSIT", "Block 2", "Palawan State University"
    , "College of Sciences", "RPS", "February", 14, 2023, "Single"]
    print(f"Name: {developer[0]}")
    print(f"Status: {developer[-1]}")
    print(f"School: {developer[-7]}")
    print(f"Department: {developer[-6]}")
    print(f"Year/Program/Block: {developer[1]} - {developer[2]} - {developer[3]}")
    print(f"Game name: {developer[-5]}")
    print(f"Date Started: {developer[-4]} {developer[-3]}, {developer[-2]}")

else: 
    print("Invalid Input!")
