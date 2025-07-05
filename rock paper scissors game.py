#ROCK PAPER SCISSORS game
import random


options=("rock","paper","scissors") # A tuple of options



score_pl=0
score_com=0
total_played=0

playing=True

while playing:
    player=input("ROCK/ PAPER/ SCISSORS? : ").lower()

    computer= random.choice(options)

    while player not in options:
        player=input("Idiot!! Enter ROCK/ PAPER/ SCISSORS? : ").lower()
    total_played+=1
    if player==computer:
        print(f"You: {player}")
        print(f"Computer:{computer}")
        print("----------------------")
        print("DRAW!!")
            
    elif player=="rock" and computer=="scissors":
        print(f"You: {player}")
        print(f"Computer:{computer}")
        print("----------------------")
        print("You WIN!!!")
        score_pl+=1

    elif player=="paper" and computer=="rock":
        print(f"You: {player}")
        print(f"Computer:{computer}")
        print("----------------------")
        print("You WIN!!!")
        score_pl+=1

    elif player=="scissors" and computer=="paper":
        print(f"You: {player}")
        print(f"Computer:{computer}")
        print("----------------------")
        print("You WIN!!!")
        score_pl+=1
    else :
        print(f"Computer:{computer}")
        print("----------------------")
        print("You LOSE :( ")
        score_com+=1
     
    resume=input("Play again(y/n): ").lower()
    if resume !="y":
        playing=False

print("---------------------------------------")
print(f"You played {total_played} times")
print(f"YOU WON {score_pl} times")



    
