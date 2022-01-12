import random

guessTaken=0

print('Hello! Whats your name?')
name=input()

number = random.randint(1,50)
print('Well '+name+' I am thinking of a number between 1 and 50.')

for guessTaken in range(6):
    print("Take a guess.")
    guess = input()
    guess = int(guess)

    if(guess<number/2):
        print('Your guess is too low')
    elif(guess<number):
        print("Your are near but little bit low than my number")
    elif(guess>number*2):
        print("Oh! You went too far")
    elif(guess<number*2 and guess != number):
        print("You are near but little bit more than my number")
    if guess==number:
        break

if guess == number:
    guessTaken = str(guessTaken+1)
    print("Good Job, "+name+"! You guessed my number in "+guessTaken+" guesses!")

if guess != number:
    number = str(number)
    print('Nope. The number I was thinking of was '+number+'.')