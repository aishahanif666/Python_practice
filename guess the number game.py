import random
rn = random.randint(1,16) 
user = input("What is your name? ")
print("HELLO",user,"!!Let's have some fun...")
print("I have thought a random number between 1 to 16.")
print("YOU HAVE 3 CHANCES!!")
counts=0
while counts<3: 
    num = int(input("Guess the number: "))
    if (num<rn): 
        print("You have entered a smaller number!")
        counts+=1
    elif (num>rn): 
        print("You have entered a greater number!")
        counts+=1
    elif (num==rn):
        print("CONGRATS!!YOU WON..")
        break
if (counts==3):
    print("YOU LOST!!TRY AGAIN..")
    print("Random number was",rn)    