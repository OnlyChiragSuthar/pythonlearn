#                 S W G
# computer =      0 1 2
# player =  S  0  D W L
#           W  1  L D W
#           G  2  W L D
import random
computer = random.choice(["S","W","G"])

play = input("Enter Your Choice With First Letter:")
player = play.upper()


if (computer=="S"):
    if(player=="S"):
        print("Draw!")
    elif (player=="W"):
        print("You Lose!")
    elif(player=="G"):
        print("You Win!")
    else:
        print("Invalid Character")

elif (computer=="W"):
    if(player=="S"):
        print("You Win!")
    elif (player=="W"):
        print("Draw!")
    elif(player=="G"):
        print("You Lose!")
    else:
        print("Invalid Character")

else:
        if(player=="S"):
            print("You Lose!")
        elif (player=="W"):
            print("You Win!")
        elif(player=="G"):
            print("Draw!")
        else:
            print("Invalid Character")




print(f"Computer's Choice:{computer}")
print(f"Playes's Choice:{player}")