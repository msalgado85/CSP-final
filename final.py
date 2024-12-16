import random
i = 0




# Generate a random number between 1 and 100
number = random.randint(1,100)
#Prompt the user for their name and welcome them to the game
name = input("Please enter your name: ") 
print(f"Well {name} I've thought of a number between 1 and 100 and you have onbly 8 tries to get it. What number do you think it is?" )
#Give the user eight tries to guess the number
while i < 8: #This is limiting the amount of tries to 8
    guess = int(input("Please guess a number: "))
    i = i + 1 #This is our counter
    if guess < number: #Checks if the guess is less than the secret number
        print(f"The number is greater than {guess}")
    elif guess == number: #The winning path
        print("You guessed it!")
        print(f"You have made {i} guesses") #Keeps track of the number of attemprs the user has made.
        #ends algorithm because the player has guessed the number correctly
        break 
    else:
        print(f"The number is less than {guess}")
if i == 8: #The losing path 
    print(f"LOSER!!! The secret number was {number}!!!!")



#On each guess, check if it is less than, greater than, or equal to the secret number
#Provide feedback to the user accordingly

#Keep track of the number of attemprs the user has made.
    
#If the user guesses the number correctly within eight attempts, congratulate them.
    
#If the user fails to guess correctly after eight attempts, reveal the number