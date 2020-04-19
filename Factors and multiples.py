#To find the factors and multiples of given number
a = int(input("Enter a number: "))
print("\nFACTORS: ")
for i in range(1,a+1):
    if a%i == 0:
        print(i,end=",")
print("\nMULTIPLES: ")
for j in range(1,11):
    b = a*j
    print(b,end=",")