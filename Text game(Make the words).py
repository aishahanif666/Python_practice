a=input("Would you like to play a game? (yes/no) ")
if a.lower() == "yes":
    print("That is great!! I will give you few letters with the help of which you have to make 3 words.. ")
    x=1
    while x<=3:
        print("h|c|n|a|i")
        b=input("1st word: ")
        if (b.lower()=="chain" or b.lower()=="chin" or b.lower()=="inch" or b.lower()=="can" or b.lower()=="ach"):
            x+=1
        else:
            print("Invalid")
            break    
        c=input("2nd word: ")
        if (c.lower()=="chain" or c.lower()=="chin" or c.lower()=="inch" or c.lower()=="can" or c.lower()=="ach"):
            x+=1
        else:
            print("Invalid")
            break    
        d=input("3nd word: ")
        if (d.lower()=="chain" or d.lower()=="chin" or d.lower()=="inch" or d.lower()=="can" or d.lower()=="ach"):
            x+=1
            print("You are awesome")
        else:
            print("Invalid")
            break
    game2=input("Do you want to continue?(yes/no) ")
    if game2.lower()=="yes":
        y=1        
        while y<=3:
            print("i|d|k|n")
            e=input("1st word: ")
            if (e.lower()=="ink" or e.lower()=="kind" or e.lower()=="kin" or e.lower()=="kid"):
                y+=1
            else:
                print("Invalid")
                break    
            f=input("2nd word: ")
            if (f.lower()=="ink" or f.lower()=="kind" or f.lower()=="kin" or f.lower()=="kid"):
                y+=1
            else:
                print("Invalid")
                break    
            g=input("3nd word: ")
            if (g.lower()=="ink" or g.lower()=="kind" or g.lower()=="kin" or g.lower()=="kid"):
                y+=1
                print("You are awesome")
            else:
                print("Invalid")
                break
    else:
        print("Thanks for playing:)")
else:
    print("That's too bad:(")
    
