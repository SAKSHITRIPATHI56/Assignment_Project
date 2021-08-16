import random

print("Let's play the game")
print("Welcome to Number Guess Game ")

a=int(input("Enter the start number : "))
b=int(input("Enter the end number : "))

attempts=0
guess=0

random_number=random.randint(a,b)
while True:
    attempts+=1
    guess=int(input("Guess the number : "))
    if guess < random_number:
        print("Sorry, guess again. Too Low")
    elif guess > random_number:
        print("Sorry, guess again. Too High")
    else:
        print(" ")
        print(f'Yes,congrats !!. You have guessed the number {random_number} correctly')
        print(" ")
        print(f'Total attempts {attempts} ')
        break
print("The game END . Thanks for Playing")
    
    
