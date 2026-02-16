import random

print(f"Welcome to game of rolling a dice")


while True:
    choice = input("Press 'Enter' To Start the dice to roll and 'q' for leaving the game")
    if choice == 'q':
        print("Thanks for your time")
        break
    elif choice == '':
        num =random.randint(1,6)
        print(f"Your num is {num}")
    else:
        print(f"Invalid \n num")    
    
print("Game is Over!")    



#Press 'Enter' To Start the dice to roll and 'q' for leaving the game 
#Your num is 2
#Press 'Enter' To Start the dice to roll and 'q' for leaving the game 
#Your num is 4
#Press 'Enter' To Start the dice to roll and 'q' for leaving the game 
#Your num is 1
#Press 'Enter' To Start the dice to roll and 'q' for leaving the game 
#Your num is 1
#Press 'Enter' To Start the dice to roll and 'q' for leaving the game 
#Your num is 5


# if we choose 'q'

#Press 'Enter' To Start the dice to roll and 'q' for leaving the gameq

#Thanks for your time
#Game is Over!
