import random

def display_title():
    print("\nThis is a guessing game. It will randomly select a number between 1 and 10. It will then\n"
          "promt the user for input to try and guess what that number is. After each guess the user will \n"
          "receive as prompt telling them if they were \"too high\" or \"too low\". When the user guesses\n"
          "the right number they will be informed and asked if they would like to play again. The game will\n"
          "continue until the user decides to quit\n")

def play_game(targetNumber, counter):
    

    while True:
        
        try:
            if counter == 1:
                # take user input and convert to an int
                playerGuess = int(input("\nOk! Lets give it a go. Please choose a number between 1 and 10: "))
                counter += 1
            elif counter >= 2:
                
                playerGuess = int(input("\nLets try again. Please choose a number between 1 and 10: "))
        except ValueError:
            print("Please enter a valid response.")
        else:
            
            if 1 > playerGuess > 10:
                print("Please pick a number between 1 and 10.")

            elif 1 <= playerGuess <= 10:
                
                

                if playerGuess > targetNumber:
                    
                    print("Sorry that is too high!")

                elif playerGuess < targetNumber:
                    
                    print("Sorry that is too low!")

                elif playerGuess == targetNumber:
                    
                    print("Good job %i was the right number!" % targetNumber)
                    return

                else:
                    
                    print("Invalid input. Please try again")

            else:
                
                print("Invalid input. Please try again.")

def main():
    

    while True:
        
        playAgain = input("\nWould you like to play (y/n)? ").lower()

        if playAgain == "y":
            
            targetNumber = random.randint(1, 10)
            counter = 1
            play_game(targetNumber, counter)

        elif playAgain == "n":
            
            print("Thanks for playing. Goodbye.")
            exit()

        else:
            print("Please enter a valid choice.")

display_title()
main()