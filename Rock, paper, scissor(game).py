#Rock, paper, Scissor game
import random
comp = 0
user = 0
comp_list=["Rock","Paper","Scissors"]
while True:
    user_choice=input('Enter "R" for Rock, "P" for Paper and "S" for Scissor: ')
    comp_choice = random.choice(comp_list)
    print("Computer's Choice:",comp_choice)
    if user_choice=="R" and comp_choice=="Paper":
        print("\nComputer got 1 point\n")
        comp+=1
        print(f"Computer Score: {comp}\nYour score: {user}\n")
    elif user_choice=="R" and comp_choice=="Scissors":
        print("\nYou got 1 point\n")
        user+=1
        print(f"Computer Score: {comp}\nYour Score: {user}\n")
    elif user_choice=="P" and comp_choice=="Rock":
        print("\nYou got a point\n")
        user+=1
        print(f"Computer Score: {comp}\nYour Score: {user}\n")
    elif user_choice=="P" and comp_choice=="Scissors":
        print("\nComputer got another point\n")
        comp+=1
        print(f"Computer Score: {comp}\nYour Score: {user}\n")
    elif user_choice=="S" and comp_choice=="Rock":
        print("\nComputer gain a point\n")
        comp+=1
        print(f"Computer Score: {comp}\nYour Score: {user}\n")
    elif user_choice=="S" and comp_choice=="Paper":
        print("\nYou got a point\n")
        user+=1
        print(f"Computer Score: {comp}\nYour Score: {user}\n")
    else:
        print("\nYou both choose the same\n")
    if user==3:
        print("You Won!!\n")
        break
    elif comp==3:
        print("Computer Won!!You've tried well...\n")
        break
print("\nGAME OVER")    
        
        
    