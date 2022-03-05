def collatz(number):
        while number!=1:
            print(number)
            if number%2==0:
                number=number//2
            else:
                number=3*number+1
try:
        collatz(int(input('Enter your number: ')))
except ValueError:
        print('Please enter integer value only.')

