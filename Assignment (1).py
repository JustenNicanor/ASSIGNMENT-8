import random
print ("Give 3 numbers from 0-9")
Samenum = 0
ran1 = random.randint(0,9)
ran2 = random.randint(0,9)
ran3 = random.randint(0,9)
Firstnum = int(input("Enter your First number: "))    
Secondnum = int(input("Enter your Second number: "))
Thirdnum = int(input("Enter your Third number: "))
for i in range(1):
    if Firstnum == ran1 or Firstnum == ran2 or Firstnum == ran3:
        Samenum += 1
    if Secondnum == ran1 or Secondnum == ran2 or Secondnum == ran3:
        Samenum += 1
    if Thirdnum == ran1 or Thirdnum == ran2 or Thirdnum or ran3:
        Samenum +=1
if  Samenum == 3:
        print("You WIN!")
else:
        print("You LOSE!")






