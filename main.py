#NUMBER GUSSING GAME
import  random

print("Welcome to a number gussing game !🎯")
print("I have selected a number between 1 and 100. Can you guess it?")
# IIT IS RUM WEHN THE CONDION BECOME FALSE.
while True:
#IT GENERATE RANDOM NUMBER FROM  1-100.
    number=random.randint(1,100) 
    attempt=0
    gusses=None

    while gusses!=number:
        try:
            gusses=int(input("Enter your gusses: ")) # It take input from the user.
            attempt+=1
            if gusses<number:
                print("Too low! ⬇️")
            elif gusses > number:
                print("Too high! ⬆️")
            else:
                print(f"Congratulations! You guessed the number {number} in {attempt} attempts 🎉")
        except ValueError:
            print("Please enter a valid integer !")

# Ask user to play again this game
    play_again=input("Do you want to play  again! (y/n): ")
    if play_again!='y':
        print("Thanks for playing! Goodbye 👋")
        break