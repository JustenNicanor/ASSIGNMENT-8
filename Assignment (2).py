def guessthenumber ():
    import random
    randomizer1 = random.randint(0,100) 
    return randomizer1
def guesser(gtnF):
    Guesser = int(input("Guess the number: "))
    if gtnF < Guesser:
        print("GREATER THAN")
        guesser(gtn)
    elif gtnF > Guesser:
        print("LESS THAN")
        guesser(gtn)
    else:
        print ("CORRECT!")

gtn = guessthenumber()
user = guesser(gtn)
