from random import choice
import os
letterList = []
letterList[:0] = 'qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM'
words = ['Apple', 'Shadow', 'Thunder', 'Winter', 'Language']
word = choice(words)
secret = ['*'] * len(word)
life = 7
isGameOver = False
while not isGameOver:   
    if life > 0:
        if '*' in secret:
            secretString = ''.join(secret)
            print(f"Secret word is: {secretString}. \nYou have {life} left.")
            guess = input("Type some letter to guess or type 'quit' to quit program: ")
            if guess in letterList and guess != '':
                if guess in word and guess not in secret:
                    os.system('cls')
                    print(f'The letter "{guess}" is in the secret word. Good job!')
                    i = 0
                    for i in range(len(word)):
                        if guess == word[i]:
                            secret[i] = secret[i].replace('*', f'{guess}')       
                elif guess in word and guess in secret:
                    os.system('cls')
                    print(f"You've already written the letter '{guess}'. Please, try another one.")
                elif guess not in word and len(guess) == 1:
                    os.system('cls')
                    print(f"The letter '{guess}' isn't in the secret word.")
                    life -= 1
            elif guess.lower() == 'quit':
                isGameOver = True
            elif guess not in letterList or guess == '' or len(guess) != 1:
                os.system('cls')
                print('Incorrect input, please try again!')
        elif '*' not in secret:
            os.system('cls')
            print(f"YOU WIN, GRATZ!")
            secretString = ''.join(secret)
            print(f"Secret word is: {secretString}.")   
            print('Press Enter to close program...') 
            input()
            break
    else:
        os.system('cls')
        print('GAME OVER')
        print('Press Enter to close program...')
        input()
        isGameOver = True