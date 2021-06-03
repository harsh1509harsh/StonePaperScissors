import random
print("Welecome the the stone/paper/scissors game.\n")
Points = [0,0]
Moves = ["Stone","Paper","Scissors"]
print("Rule :  One who wins the 3 match first will won the match!\n ")
while 1:
    try:
        UserChoose = int(input("Options: \nStone (1)\nPaper (2)\nScissors (3)\nEnter your choice: "))
        UserChoose = Moves[UserChoose-1]
        ComChoose = random.randint(0,2)
        ComChoose = Moves[ComChoose]
        if UserChoose == ComChoose:
            print("Draw")
        else:
            if( UserChoose == "Stone" and ComChoose == "Scissors") or (UserChoose == "Paper" and ComChoose == "Stone") or (UserChoose == "Scissors" and ComChoose == "Paper") :
                print(UserChoose + " vs. " + ComChoose + "\nUser Wins\n")
                Points[0] += 1
            else:
                print(UserChoose + " vs. " + ComChoose + "\nComputer Wins\n")
                Points[1] += 1
        if max(Points) == 3:
            break
    except:
        print('\nPlease choose only from the repective\nnumbers given in front of the options :-)\n')
print(f'\nUser Points: {Points[0]}\nComputer Points: {Points[1]}\n')
print('User wins!' if Points[1] < Points[0] else 'Computer Wins!\n')
