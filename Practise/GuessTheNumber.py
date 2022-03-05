print('Hello and welcome to my program of guessing the no.\nCan I please know your name?')
name=input()
print(f'Hello {name}, Let\'s Begin our game')
      
import random
secret_number=random.randint(1,20)
print('I am thinking of a number between 1 and 20')

for guesses_taken in range(1,6):
    print('Take a guess')
    guess=int(input())

    if guess>secret_number:
        print('Your guess is higher than the guessed no.')
    elif guess<secret_number:
        print('Your guess is lower than the guessed no.')
    else:
        print(f'Congrats {name}, You are correct.')
        break

if guess==secret_number:
    print(f'You guessed the no. in {guesses_taken} tries')
else:
    print(f'Nope, my number was {secret_number5}, Better Luck next time.')
