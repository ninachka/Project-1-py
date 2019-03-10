#For understanding random module has been reviewed  the following link
#https://docs.python.org/3/library/random.html?highlight=random#module-random


import random
    
def start_game():
    print("""
**************************************
* Welcome to a Number Guessing Game! *
**************************************
         """)
    guess = random.randint(1,10)  #Generating a random number that the player has to guess
    number_of_attempt = 0         #Calculating number of attempts
    
    while True: 
        player_guess = input("Pick up one of the number from 1 to 10: ")  #Players choosen number
        number_of_attempt += 1    #Increasing number of guess by 1 after every try
           
        try:
            player_guess = int(player_guess)  #Converting user input into integer
        except ValueError:
            print("Please choose a number beetween 1 and 10")
               
        else:
            if player_guess < guess:
                print("It is higher")
            
            elif player_guess > guess:
                print("It is lower")
            
            else:
                break
    print("Good job! Your the number of attempts is {}".format(number_of_attempt))         
    play_again = input("Would you like to contine to play (YES/NO) ")
    if play_again.upper() == "YES":
        start_game()
    else:
        print (" Thank you for playing with us!")
    
if __name__ == '__main__':
    # Kick off the program by calling the start_game function.
    start_game()
