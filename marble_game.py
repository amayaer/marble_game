
import random

def play_game():
    print ("************************************************")
    print ("         Welcome to the Challenge!     ")
    print ("Both you and the computer start with 5 marbles.")
    print (   "The first to get all 10 marbles wins! ")
    print ("************************************************\n")



    cmarbles = 5
    pmarbles = 5
    turns = 0


    while cmarbles != 10 and pmarbles != 10:
        print("\U0001F535 The computer is hiding some marbles...can you guess?\n")
        guess = input("\U0001F914 Do you think the number is Even(0) or Odd(1)?: ")
        compChoice = random.randint(1,cmarbles)

        if compChoice %2 == int(guess):
            print (f"\U00002705 Correct! The computer hid {compChoice} marbles.\n")
            pmarbles += compChoice
            cmarbles -= compChoice
            turns +=1 
            print(f"Current results after {turns} turns: ")
            print("----------------------------------------")
            print(f"Player:   {pmarbles} marbles")
            print(f"Computer: {cmarbles} marbles")
            print("----------------------------------------\n")

            if cmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ") 
                print("************************************************")
                print()
                print ("The computer wins! Better luck next time!")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n") 
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.") 
            
            if pmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ")
                print("************************************************")
                print()
                print("**\U0001F389 CONGRATUALTIONS! You won all 10 marbles!**")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n")
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.") 
           

        elif compChoice%2 != 0 and int(guess) == 1:
            print (f"\U00002705 Correct! The computer hid {compChoice} marbles.")
            print()
            pmarbles += compChoice
            cmarbles -= compChoice
            turns +=1 
            print(f"Current results after {turns} turns: ")
            print("----------------------------------------")
            print(f"Player:   {pmarbles} marbles")
            print(f"Computer: {cmarbles} marbles")
            print("----------------------------------------")
            print()

            if cmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ") 
                print("************************************************")
                print()
                print ("The computer wins! Better luck next time!")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n") 
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.") 
            

            if pmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ")
                print("************************************************")
                print()
                print("**\U0001F389 CONGRATUALTIONS! You won all 10 marbles!**")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n") 
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.")       
           

        else:
            print(f"\U0000274C Wrong! The computer hid {compChoice} marbles")
            print()
            pmarbles -= 1
            cmarbles += 1
            turns +=1 
            print(f"Current results after {turns} turns: ")
            print("----------------------------------------")
            print(f"Player:   {pmarbles} marbles")
            print(f"Computer: {cmarbles} marbles")
            print("----------------------------------------")
            print()

            if cmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ") 
                print("************************************************")
                print()
                print ("The computer wins! Better luck next time!")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n") 
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.") 
            

            if pmarbles == 10:
                print("************************************************")
                print("                   GAME OVER                    ")
                print("************************************************")
                print()
                print("**\U0001F389 CONGRATUALTIONS! You won all 10 marbles!**")
                print()
                again = input ("Do you want to play again? (y or n): ").lower()
                print()
                if again == "n":
                    print("Thank you for playing! Goodbye!")
                    return

                elif again == "y":
                    print("Restarting the game....\n") 
                    play_game()

                else:
                    print("Invalid input! Please enter 'y' or 'n'.") 
            

        

        print("\U0001F7E0 Now it is your turn to hide some marbles...")
        print()
        pChoice = int(input("...Enter how many marbles you want to hide (1-9): "))
        print()
        compGuess = random.randint(0,1)
        

        if pChoice %2 == 0 and compGuess == 0:
            print("\U0001F4BB The computer guesses even.")
            print (f"The computer was right! You hid {pChoice} marbles.")
            pmarbles -= pChoice
            cmarbles += pChoice 
            turns +=1 
            print()

        elif pChoice %2 != 0 and compGuess == 1:
            print("\U0001F4BB The computer guesses odd.")
            print(f"The computer was right! You hid {pChoice} marbles.")
            pmarbles -= pChoice
            cmarbles += pChoice 
            turns +=1 
            print()

        elif pChoice %2 != 0 and compGuess == 0: 
            print("\U0001F4BB The computer guesses even.")
            print (f"\U0000274C The computer was wrong! You hid {pChoice} marbles.")
            pmarbles += 1
            cmarbles -= 1 
            turns +=1 
            print()

        else:
            print ("\U0001F4BB The computer guesses odd.")
            print (f"\U0000274C The computer was wrong! You hid {pChoice} marbles.")
            pmarbles += 1
            cmarbles -= 1 
            turns +=1 
            print()


        print()
        print(f"Current results after {turns} turns: ")
        print("----------------------------------------")
        print(f"Player:   {pmarbles} marbles")
        print(f"Computer: {cmarbles} marbles")
        print("----------------------------------------")
        print()



        if cmarbles == 10: 
            print("************************************************")
            print("                   GAME OVER                    ") 
            print("************************************************")
            print()
            print ("The computer wins! Better luck next time!")
            print()
            again = input ("Do you want to play again? (y or n): ").lower()
            print()
            if again == "n":
                print("Thank you for playing! Goodbye!")
                return

            elif again == "y":
                print("Restarting the game....\n") 
                play_game()
            

            else:
                print("Invalid input! Please enter 'y' or 'n'.") 

        

        if pmarbles == 10:
            print("************************************************")
            print("                   GAME OVER                    ") 
            print("************************************************")
            print()
            print("**\U0001F389 CONGRATUALTIONS! You won all 10 marbles!**")
            print()
            again = input ("Do you want to play again? (y or n): ").lower()
            print()
            if again == "n":
                print("Thank you for playing! Goodbye!")
                return

            elif again == "y":
                print("Restarting the game....\n") 
                play_game()

            else:
                print("Invalid input! Please enter 'y' or 'n'.") 

        
    
play_game()        
                

    


