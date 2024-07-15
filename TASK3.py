import random
choices = ["rock","paper","scissors"]

def UserChoice():
    while True:
        move = input("Enter rock , paper , or scissors ").lower()
        if move in choices:
            return move 
        else:
            print("Invalid Choice Plese Enter rock , paper , or scissors...")
def computer_choice():
    return random.choice(choices)

def  winner(UserChoice,computer_choice):
    if UserChoice==computer_choice:
        return "It's a tie!"
    elif(UserChoice == "rock" and computer_choice == "scissors")or\
        (UserChoice == "scissors" and computer_choice == "paper")or\
        (UserChoice == "paper" and computer_choice == "rock"):
        return " ''''You win Congrates''' "
    else:
        return " You Lose The Game "

def gametime():
    while True:
        uc = UserChoice()
        cc = computer_choice()

        print(f"\nYou chose: {uc}")
        print(f"Computer chose: {cc}")

        result=winner(uc,cc)
        print(result)

        play_again= input("\nDo you want to play again? (yes/no): " ).lower()
        if play_again!="yes":
            print("Thanks For Playing!")
            break 
if __name__ == "__main__":
    print("Welcome to Rock, Paper, Scissors!\n")
    gametime() 
        
     
