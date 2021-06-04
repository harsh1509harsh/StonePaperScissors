import random
import sys
try:
    from colored import fore as Fore, style as Style
except ModuleNotFoundError:
    sys.system('pip3 install colored')

class IconicDecorator(object):
    def __init__(self):
        self.PASS = Style.BLINK + Fore.GREEN + "[ ✔ ]" + Style.RESET
        self.FAIL = Style.BLINK + Fore.RED + "[ ✘ ]" + Style.RESET
        self.WARN = Style.BLINK + Fore.YELLOW + "[ ! ]" + Style.RESET
        self.HEAD = Style.BLINK + Fore.CYAN + "[ # ]" + Style.RESET
        self.CMDL = Style.BLINK + Fore.BLUE + "[ → ]" + Style.RESET
        self.STDS = "     "

class StatusDecorator(object):
    def __init__(self):
        self.PASS = Style.BLINK + Fore.GREEN + "[ SUCCESS ]" + Style.RESET
        self.FAIL = Style.BLINK + Fore.RED + "[ FAILURE ]" + Style.RESET
        self.WARN = Style.BLINK + Fore.YELLOW + "[ WARNING ]" + Style.RESET
        self.HEAD = Style.BLINK + Fore.CYAN + "[ SECTION ]" + Style.RESET
        self.CMDL = Style.BLINK + Fore.BLUE + "[ COMMAND ]" + Style.RESET
        self.STDS = "           "

class MessageDecorator(object):
    def __init__(self, attr):
        ICON = IconicDecorator()
        STAT = StatusDecorator()
        if attr == "icon":
            self.PASS = ICON.PASS
            self.FAIL = ICON.FAIL
            self.WARN = ICON.WARN
            self.HEAD = ICON.HEAD
            self.CMDL = ICON.CMDL
            self.STDS = ICON.STDS
        elif attr == "stat":
            self.PASS = STAT.PASS
            self.FAIL = STAT.FAIL
            self.WARN = STAT.WARN
            self.HEAD = STAT.HEAD
            self.CMDL = STAT.CMDL
            self.STDS = STAT.STDS

    def SuccessMessage(self, RequestMessage):
        print(self.PASS + " "  + Fore.GREEN + RequestMessage + Style.RESET)

    def FailureMessage(self, RequestMessage):
        print(self.FAIL + " "  + Fore.RED + RequestMessage + Style.RESET)

    def WarningMessage(self, RequestMessage):
        print(self.WARN + " "  + Fore.YELLOW + RequestMessage + Style.RESET)

    def SectionMessage(self, RequestMessage):
        print(self.HEAD + " " + Fore.CYAN + Style.BLINK + RequestMessage + Style.RESET)

    def CommandMessage(self, RequestMessage):
        return self.CMDL + " " + Style.RESET + Fore.BLUE + RequestMessage + Fore.GREEN

    def GeneralMessage(self, RequestMessage):
        print(self.STDS + " "  + RequestMessage + Style.RESET)

mesgdcrt = MessageDecorator("icon")
ALL_COLORS = [Fore.GREEN, Fore.RED, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]
RESET_ALL = Style.RESET

print("Welecome to the Stone/Paper/Scissors game.\n")
Points = [0,0] 
Moves = ["Stone","Paper","Scissors"]
print("Rule :  One who wins the 3 match first will won the match!\n ")
while 1:
    try:
        UserChoose = int(input(mesgdcrt.CommandMessage("Options: \nStone (1)\nPaper (2)\nScissors (3)\nEnter your choice: ")))
        UserChoose = Moves[UserChoose-1]
        ComChoose = random.randint(0,2)
        ComChoose = Moves[ComChoose]
        print()
        if UserChoose == ComChoose:
            mesgdcrt.SectionMessage("Both Choose the same option\n it's a Draw\n")
        else:
            if( UserChoose == "Stone" and ComChoose == "Scissors") or (UserChoose == "Paper" and ComChoose == "Stone") or (UserChoose == "Scissors" and ComChoose == "Paper") :
                mesgdcrt.SuccessMessage(UserChoose + " vs. " + ComChoose + "\nUser Wins\n")
                Points[0] += 1
            else:
                mesgdcrt.FailureMessage(UserChoose + " vs. " + ComChoose + "\nComputer Wins\n")
                Points[1] += 1
        if max(Points) == 3:
            break
    except:
        mesgdcrt.WarningMessage('Please choose only from the repective\nnumbers given in front of the options :-)\n')
mesgdcrt.GeneralMessage(f'\nUser Points: {Points[0]}\nComputer Points: {Points[1]}\n')
if Points[0]<Points[1]:
    mesgdcrt.FailureMessage(f'Computer wins by {Points[1]-Points[0]} points')
else:
    mesgdcrt.SuccessMessage(f'User wins by {Points[0]-Points[1]} points')
