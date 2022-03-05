#6 sections for Rock Paper Scissor Game
#1st Section- Intro
#2nd Section- Variable for Win,Loss,Tie
#3rd Section- Main game loop and input Loop
#4th Section- display Player turn
#5th Section- display and choose Comp. turn 
#6th Section- Score

#1st
import random,sys
print('Hello, Lets play rock paper scissor')

#2nd
w=0
l=0
t=0

#3rd
while True:
    print(f'{w} Wins {l} Losses {t} Ties')
    while True:
        print('Enter your move : rock, paper or scissor or type quit if u want to quit')
        pm=input()
        if pm=='quit':
            sys.exit()
        elif pm=='rock' or pm=='paper' or pm=='scissor':
            break
        print('Please type rock, paper, or quit only')

#4th 
    if pm=='rock':
        print('Rock versus...')
    elif pm=='paper':
        print('Paper versus...')
    elif pm=='scissor':
        print('Scissor versus...')

#5th
    rn=random.randint(1,3)
    if rn==1:
        cm='rock'
        print('Rock')
    elif rn==2:
        cm='paper'
        print('Paper')
    elif rn==3:
        cm='scissor'
        print('Scissor')

#5th
    if pm==cm:
        print('Its a tie')
        t=t+1
    elif pm=='rock' and cm=='paper':
        print('You Lose!')
        l=l+1
    elif pm=='rock' and cm=='scissor':
        print('You Win!')
        w=w+1
    elif pm=='paper' and cm=='scissor':
        print('You Lose!')
        l=l+1
    elif pm=='paper' and cm=='rock':
        print('You Win!')
        w=w+1
    elif pm=='scissor' and cm=='rock':
        print('You Lose!')
        l=l+1
    elif pm=='scissor' and cm=='paper':
        print('You Win!')
        w=w+1
    
