#!/usr/bin/python3

import random
import time
print("""           Smash! Wrap! Cut!
    ********************************
        Rock! Paper! Scissors!
        **********************
                Welcome!
                *******
""")
player = input("Enter Player Name: ")
score_player = 0
score_ai = 0
games_played = 0
ai_wins = 0
player_wins = 0
draw_games = 0
#start = time.clock()
#while time.clock() - start < 3:
#   rand_int = random.randrange(1, 4)

while (True):
    try:
        gamble = eval(input("Choose 1, 2 or 3 to play:\n 1.Rock\n 2.Paper\n 3.Scissors\n 4.EXIT - to see scores!  \n_-_-_-_-_-_ : "))
        
        if (gamble == 4):
            break
        start = time.clock()
        while time.clock() - start < 0.1:
            rand_int = random.randrange(1, 4)
        if (gamble == rand_int):
            print("You played {}, AI played {}".format(gamble, rand_int))
            print("It's a draw, let's go again!")
        elif (gamble == 1) and (rand_int == 2):
            print("You played Rock, AI played Paper")
            print("You Lose, paper wraps rock, AI Wins!")
        elif (gamble == 1) and (rand_int == 3):
            print("You played Rock, AI played Scissors")
            print("You Win, Rock crashes Scissors, AI Loses!")
        elif (gamble == 2) and (rand_int == 3):
            print("You played Paper, AI played Scissors")
            print("You Lose, Scissors cuts paper, AI Wins!")
        elif (gamble == 2) and (rand_int == 1):
            print("You played Paper, AI played Rock")
            print("You Win, paper wraps rock, AI Loses!")
        elif (gamble == 3) and (rand_int == 1):
            print("You played Scissors, AI played Rock")
            print("You Lose, Rock crashes Scissors, AI Wins!")
        elif (gamble == 3) and (rand_int == 2):
            print("You played Scissors, AI played Paper")
            print("You win, Scissors cuts paper, AI loses!")
    except ValueError:
        print("Make Sure to enter 1, 2 or 3 to enjoy Playing R,P,S!")
        continue
    except NameError:
        print("Make Sure to enter 1, 2 or 3 to enjoy Playing Rock, Paper, Scissors!")
        continue
    except:
        break
    if gamble == rand_int:
        score_ai += 1
        score_player += 1
        draw_games += 1
        games_played += 1
    elif gamble == 1 and rand_int == 2:
        score_ai += 3
        ai_wins += 1
        games_played += 1
    elif (gamble == 1) and (rand_int == 3):
        score_player += 3
        player_wins += 1
        games_played += 1
    elif (gamble == 2) and (rand_int == 3):
        score_ai += 3
        ai_wins += 1
        games_played += 1
    elif (gamble == 2) and (rand_int == 1):
        score_player += 3
        player_wins += 1
        games_played += 1
    elif (gamble == 3) and (rand_int == 1):
        score_ai += 3
        ai_wins += 1
        games_played += 1
    elif (gamble == 3) and (rand_int == 2):
        score_player += 3
        player_wins += 1
        games_played += 1
print("*" * 40)
print("Every win earned you 3 points")
print("Every draw earned you 1 point")
print("Every loss equals 0 points")
print("*" * 40)
print("Scores:")
print("AI: {}".format(score_ai))
print("{}: {}".format(player, score_player))
print("Games Played: {}".format(games_played))
print("*" * 40)
print("AI won {} games".format(ai_wins))
print("{} won {} games".format(player, player_wins))
print("You drew {} times".format(draw_games))
print("*" * 40)

draw_odds = (draw_games / games_played) + 1
if (ai_wins > player_wins):
    print("\nNot Lucky, Try Next Time!")
elif (player_wins > ai_wins):
    print("Congratulations Lucky Fuck!")
elif (ai_wins == player_wins):
    print("What are the odds you drew with an Artificial Intelligence?")
    print("The AI can tell you: {:.2f} are the odds MF!".format(draw_odds))