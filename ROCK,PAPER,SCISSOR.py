import random
user_score=0
computer_score=0
while True:

    user_input=input("ENTER YOUR CHOICE rock, paper, scissor : \n  ")

    options = ["rock","paper","scissor"]
    computer_choice = random.choice(options)

    print("Your choice:",user_input)
    print("The Computer has chosen :",computer_choice)

    if(user_input==computer_choice):
        print("Its a Tie")

    elif(user_input=="rock" and computer_choice=="paper"):
        print("You Lost")
        computer_score=computer_score + 1

    elif(user_input=="rock" and computer_choice=="scissor"):
        print("Yea!! You Won")
        user_score=user_score + 1

    elif(user_input=="paper" and computer_choice=="rock"):
        print("Yea!! You Won")
        user_score=user_score + 1

    elif(user_input=="paper" and computer_choice=="scissor"):
        print("You Lost")
        computer_score=computer_score + 1

    elif(user_input=="scissor" and computer_choice=="rock"):
        print("You Lost")
        computer_score=computer_score + 1

    elif(user_input=="scissor" and computer_choice=="paper"):
        print("Yea!! You Won")
        user_score=user_score + 1

    else:
        print("INVALID")
    
    ask=input("\nEnter yes for continuing or exit to end game: ")
    if(ask=="exit"):
        print(f"Your score = {user_score} \ncomputer's score = {computer_score}")
        if(user_score > computer_score):
            print("HURRAY!! You Won the Game Overall")
        elif(user_score == computer_score):
            print("Its a Tie Overall")
        elif(user_score < computer_score):
            print("You Lost by Overall Score...Better Luck Next Time")
        break
    else:
        pass


        