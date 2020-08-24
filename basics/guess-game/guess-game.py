import random

guessedNumber = random.randint(1, 9)
attemptsCount = 3
answer = int(input("Guess: "))
yourAttempt = 1
while yourAttempt <= attemptsCount:    
    if answer == guessedNumber:
        print("Hurray! It's a correct answer, gratz!")
        break
    elif yourAttempt < attemptsCount and answer != guessedNumber:
        yourAttempt += 1
        answer = int(input("Guess again: "))
    elif yourAttempt == attemptsCount and answer != guessedNumber:
        print('You failed!')
        break
