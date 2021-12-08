def guesser():
    import random
    randomizer1 = random.randint(0,100)
    Guesser = int(input("Guess the number: "))
    if randomizer1 < Guesser:
        print("GREATER THAN")
        guesser()
    elif randomizer1 > Guesser:
        print("LESS THAN")
    else:
        print ("CORRECT!")
guesser()
