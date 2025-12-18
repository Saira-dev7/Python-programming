import random
number=random.randint(1,10)
guess=0
attempts=0
score=0

while attempts<3:
    guess=int(input("Guess a number from (1 to 10):   "))
    attempts+=1

    if guess < number:
        print("Too LOW!")
    elif guess > number:
        print("TOO HIGH!")
    else:
        print("GREAT! YOU GOT IT.")
if guess != number:
    print("OUT of attempts! The number was ", number)        
print("YOUR SCORE", score)