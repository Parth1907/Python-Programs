import random
sampleSpace=[]
#Generates a list comprising of Heads or tails from 10,000 times toss 
for experimentNumber in range(10000):
    outcome=random.randint(0,1)
    if outcome==0:
        sampleSpace.append('H')
    else:
        sampleSpace.append('T')
#Checks for streak of head or tail in the list
a=''.join(sampleSpace)
b=a.count('HHHHHH')
c=a.count('TTTTTT')
numberOfStreaks=b+c
print('Total Chance of head and tail streak is %s%%' % (numberOfStreaks/100))
