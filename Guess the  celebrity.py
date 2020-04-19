a=input("What is your name? ")
print(f"Hey {a}!!Let's have some fun!!\nHere are some names of famous celebrities;\n1. Johnny Depp\n2. Leanardo Dicaprio\n3. Emma Watson\n4. Kristen Stewart\n5. Keanu Reaves\nI will guess the celebrity which you thought out of the names I mentioned")
b=input("Is your character a male? (yes/no) ")
if b.lower()=="yes":
    c=input("Has your character ever played role of a pirate? (yes/no) ")
    if c.lower()=="yes":
        d=input("Is he above 50?(yes/no) ")
        if d.lower()=="yes":
            print("You thought of Johnny Depp!!")
            print("HOPE YOU ENJOYED!!")
    elif c.lower()=="no":
        e=input("Is your character played in a real based movie?(yes/no) ")
        if e.lower()=="yes":
            f=input("Has he played leading role in TITANIC(yes/no) ")
            if f.lower()=="yes":
                print("You thought of Leanardio Dicaprio!!")
                print("HOPE YOU ENJOYED!!")
        elif e.lower()=="no":
            g=input("Has your character played role of JOHN WICK? (yes/no) ")
            if g.lower()=="yes":
                h=input("Has he played leading role in MATRIX? (yes/no) ")
                if h.lower()=="yes":
                    print("You thought of Keanu Reaves!!")
                    print("HOPE YOU ENJOYED!!")
elif b.lower()=="no":
    i=input("Is your character be the part of a film series? (yes/no) ")
    if i.lower()=="yes":
        j=input("Is your character is famous because of TWILIGHT? (yes/no) ")
        if j.lower()=="yes":
            print("You thought of Kristen Stewart!!")
            print("HOPE YOU ENJOYED!!")
        elif j.lower()=="no":
            k=input("Is she the part of HARRY PORTER? (yes/no) ")
            if k.lower()=="yes":
                print("You thought of Emma Watson!!")
                print("HOPE YOU ENJOYED!!")                
       