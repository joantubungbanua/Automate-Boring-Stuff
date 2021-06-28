''' 
logic: 


1) Set a random target number 
2) if user input < target number -> say too low 
3) if user input > target number -? say too high 
4) if input == target, good job you guessed it 

'''

import random 

secretNumber = random.randint(1,20)
print ('I am thinking of a number between 1 and 20')

for guessesTaken in range(1,7): 
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber: 
        print('Too Low')
    elif guess > secretNumber: 
        print ('Too high')
    else: 
        break

if guess == secretNumber: 
    print('You got it in' + str(guessesTaken) + 'guesses')
else:  
    print('nope. my number was ' + str(secretNumber))
    




