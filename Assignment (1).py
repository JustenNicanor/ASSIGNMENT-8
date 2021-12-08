print ("Give 3 numbers from 0-9")
def lottery():
    import random
    global ran1
    global ran2
    global ran3
    ran1 = random.randint(0,9)
    ran2 = random.randint(0,9)
    ran3 = random.randint(0,9)
    if ran1 == ran2 or ran1 == ran3:
        lottery()
    elif ran2 == ran3:
        lottery()
    else:
        usernumber()
def usernumber():
    samenum = 0
    Firstnum = int(input("Enter your First number: "))    
    Secondnum = int(input("Enter your Second number: "))
    Thirdnum = int(input("Enter your Third number: "))
    for i in range(1):
        if ran1 == Firstnum or  ran1 == Secondnum or ran1 == Thirdnum:
            samenum += 1
        if ran2 == Firstnum or ran2 == Secondnum or ran2 == Thirdnum:
           samenum += 1
        if ran3 == Firstnum or ran3 == Secondnum or ran3 == Thirdnum:
            samenum +=1
    if  samenum == 3:
        print("You WIN!")
        Tryagain()
    else:
        print("You LOSE!")
        Tryagain()
def Tryagain():
    print("Type 'y' for YES if you want to play again, Type 'n' for NO.")
    Pagain = input("Do you want to play again? ")
    if Pagain =='y':
        lottery()
    elif Pagain =='n':
        print("Thankyou for playing!")
    else:
        Tryagain()
        
    




lottery()






