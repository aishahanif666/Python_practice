#Nested for loops

a = int(input("How many tables you wanna print? "))
b = int(input("How many multiples you want? "))
for i in range(1,a+1):
    print("\nTABLE:",i,"\n----------")
    for j in range(1,b+1):    
        print(f"{i} * {j} = {i*j}")
        