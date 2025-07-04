import random as r


lower=int(input("Enter lower bound: "))
upper=int(input("Enter upper bound: "))

answer=r.randint(lower,upper)

num_guess=0

while True:
    guess=input(f"Guess an integer between {lower} to {upper} (press 'q' to exit) :")
    if guess.lower()=='q' or not guess.isdigit():
        print("Such a Loser.. Can't even guess a Integer")
        break
    elif int(guess)<lower or int(guess)>upper:
        print("INVALID GUESS! Guess between the range")
    else:
        if int(guess)<answer:
            print("Incorrect! Guess Higher")
            num_guess+=1
        elif int(guess)>answer:
            print("Incorrect! Guess Lower!!")
            num_guess+=1
        else:
            print("CORRECT!!!")
            num_guess+=1
            break
    
print()
print("-------------------------------------")        
print(f"The Answer is {answer}")
print(f"Total number of Guesses : {num_guess}")



 
