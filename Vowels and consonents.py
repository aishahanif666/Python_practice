a = input("ENTER A STRING: ")
b = a.lower()
print(b)
print("-------------------")
print("LENGTH: ",len(a))
vowel = "aeiou"
v = 0
c = 0
for i in a:
    if i in vowel:
        v+=1
    else:
       c+=1
print("VOWELS:",v)
print("CONSONENTS:",c)
       