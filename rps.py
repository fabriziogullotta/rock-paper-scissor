import random

options = ["rock","paper","scissor"]
win = "You win!"
tie = "Tie!"
lose = "You lose!"
invalid = "Invalid choice"
run = True;

def win_conditions(player_option,com_option):
    if player_option == "rock":
        match com_option:
            case "rock":
                return tie
            case "paper":
                return lose
            case "scissor":
                return win
    elif player_option == "paper":
        match com_option:
            case "rock":
                return win
            case "paper":
                return tie
            case "scissor":
                return lose
    elif player_option == "scissor":
        match com_option:
            case "rock":
                return lose
            case "paper":
                return win
            case "scissor":
                return tie
        
def main(run):
    com_option = options[random.randrange(0,len(options),1)].lower()
    while run:
        player_option = input("Rock, Paper or Scissor?\n").lower()
        if player_option in options:
            print("#################")
            print('Player:'+player_option.capitalize())
            print('COM:'+com_option.capitalize())
            print("#################")
            print(win_conditions(player_option,com_option))
            run = False
        elif player_option == "quit" or player_option == "q":
            run = False
        else:
            print(invalid)
    
if __name__ == "__main__":
    main(run)

