import random

correctNum = random.randint(1,9)

guess1 = int(input("I picked a number from 1-9, can you guess what it is? "))

if(guess1>correctNum):
    guess2 = int(input("Not quite, try guessing lower "))
elif(guess1<correctNum):
    guess2 = int(input("Try again but this time, try guessing a little higher "))
else:
    print("Wow! You got it! Great Job!")

if(guess2>correctNum):
    guess3 = int(input("Not quite, try guessing lower "))
elif(guess2<correctNum):
    guess3 = int(input("Try again but this time, try guessing a little higher "))
else:
    print("Wow! You got it! Great Job!")

if(guess3>correctNum):
    guess4 = int(input("Not quite, try guessing lower "))
elif(guess3<correctNum):
    guess4 = int(input("Try again but this time, try guessing a little higher "))
else:
    print("Wow! You got it! Great Job!")

if(guess4>correctNum):
    guess5 = int(input("Not quite, try guessing lower "))
elif(guess4<correctNum):
    guess5 = int(input("Try again but this time, try guessing a little higher "))
else:
    print("Wow! You got it! Great Job!")

if(guess5>correctNum):
    print("Game Over")
elif(guess5<correctNum):
    print("Game Over")
else:
    print("Wow! You got it! Great Job!")