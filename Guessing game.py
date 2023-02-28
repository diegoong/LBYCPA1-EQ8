import random
                                                
correct_number = random.randint(0, 45)                                                      #Generate a random integer between 0 and 45
                                                                    
chances = 10                                                                                #Set the number of chances the user has to guess the number
num_attempts = 0                                                                            #Attempt tracker is set to 0 


for i in range(chances):                                                                    #10 chances to guess the correct numnber
    
    guess = int(input("Guess a number between 0 and 45: "))                                 #Get the user's guess as an integer
    num_attempts +=1                                                                        #Track the number of attempts

    
    if guess == correct_number:                                                             #Check if the guess is correct
        print("Hooray, you got the correct number!")
        print("It took you", num_attempts, "attempt/s to guess the correct number")        #Tells the user the number of attempts it took him/her to guess the correct number
        break                                                                               # Exit the loop if the guess is correct
    
    
    elif guess > correct_number:                                                            #Provide a hint to the user if the guess is too high or too low
        print("Your guess is too high. Guess lower!")
    else:
        print("Your guess is too low. Guess higher!")
    
    
    print("You have", chances - i - 1, "chance/s left.")                                   #Let the user know how many chances they have left
    
    
else:
    print("Better luck next time! The secret number is", correct_number)                   #Reveal the correct number if the user runs out of chances
