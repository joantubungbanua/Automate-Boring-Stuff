'''
collatz(number):
    if(number == even):
        return(number //2)
    if it's odd:
        return ( 3 * number + 1)
    else: 
        enter an actual number
    
if number that returned != 1: 
    collatz 
else: 
    break;  

'''

'''
input = 4

input = 5 


'''

def int_input(prompt): 
    while True: 
        try:
            age = int(input(prompt))
            return age
        except ValueError as e: 
            print("This isn't an integer. Try again.")



def collatz(number): 

    print(number)

    if (number == 1 ): 
        return 1
    else: 
        if( number % 2 == 0): 
            return(collatz(number // 2))

        elif ( number% 2 == 1): 
            return( collatz(3 * number + 1))
    
    
    

def main(): 
    userInput = int_input("Enter a number: ")
    collatz(userInput)
    
  
        

if __name__ == "__main__":
    main()