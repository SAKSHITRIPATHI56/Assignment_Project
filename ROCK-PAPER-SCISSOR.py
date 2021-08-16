import random

print("LET'S  START THE GAME ..........")
print("Welcome to ROCK-PAPER-SCISSOR ")

comp_win = 0
player_win = 0


def choose_options():
    player_choice = input("Choose  Rock, Paper or Scissors : ")
    player_choice.upper()
    if  player_choice in ["Rock", "rock", "ROCK", "r","R", "1"]:
        player_choice = "r"
    elif  player_choice in ["Paper", "PAPER", "paper","p","P", "2"]:
        player_choice = "p"
    elif  player_choice in ["Scissors","SCISSORS",  "scissors","s","S","3"]:
        player_choice = "s"
    else :
        print("I don't understand, Try again ")
        choose_option()
    return player_choice

def computer_options() :
    
    comp_choice = random.randint(1,3)
    if comp_choice == 1:
        comp_choice = "r"
    elif comp_choice == 2 :
        comp_choice = "p"
    else :
        comp_choice = "s"
    return comp_choice

while True :
    
    print(" ")
    player_choice = choose_options()
    comp_choice = computer_options()
    print(" ")

    if player_choice == "r" :
        if comp_choice == "r" :
            print("You choose rock. The computer also choose rock. \n It's a TIE ")
        elif comp_choice == "p" :
            print("You choose rock. The computer  choose paper. ")
            print("Paper covers Rock. \n You lose.")
            comp_win += 1
        elif comp_choice == "s" :
            print("You choose rock. The computer  choose scissor. ")
            print("Rock smashes SCISSOR. \n You win.")
            player_win += 1
    elif player_choice == "p" :
        if comp_choice == "p" :
            print("You choose paper. The computer also choose paper. \n It's a TIE ")
        
        elif comp_choice == "r" :
            print("You choose paper. The computer  choose rock. ")
            print("Paper covers Rock. \n You win.")
            player_win += 1

        elif comp_choice == "s" :
            print("You choose paper. The computer  choose scissor. ")
            print("SCISSOR tears PAPER. \n You lose.")
            comp_win += 1

    elif player_choice == "s" :
        if comp_choice == "s" :
            print("You choose scissor. The computer also choose scissor. \n It's a TIE")
        
        elif comp_choice == "p" :
            print("You choose scissor. The computer  choose paper. ")
            print("SCISSOR tears PAPER. \n You win.")
            player_win += 1

        elif comp_choice == "r" :
            print("You choose rock. The computer  choose scissor. ")
            print("Rock smashes SCISSOR. \n You lose.")
            comp_win += 1

    print(" ")
    print("Player win : " + str (player_win))
    print("Computer win : " + str (comp_win))
    print(" ")

    player_choice = input("Do you want to play again? (Y/N)")
    if player_choice in ["Y", "YES","y", "yes"] :
        pass
    elif player_choice in ["N", "NO", "n", "no"]:
        break
    else :
        break

    
    
    

