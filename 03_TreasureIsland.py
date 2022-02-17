print('''
*******************************************************************************
|                   |                  |                     |
_________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
|                `"=._o`"=._      _`"=._                     |
_________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
         |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
_________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
                                         ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇

first_choice = input("Nice of the princess to invite us over for a picnic, eh Luigi? Do we turn left or right to enter the Koopa castle?").lower()
#Anything other than left is death.
if (first_choice != "left"):
    print ("You've taken a wrong turn and fallen into quicksand. Better luck next time.")
else:
    second_choice = input("Uhhhhh I dunno Mario, that river is looking pretty fierce. Do we wait or try to swim across it?").lower()
    if (second_choice != "wait"):
        print ("The water was too fierce even for our heroes. You drowned.")
    else:
        door_choice = input("You come to Koopa castle and are presented with a Red, Yellow, and a Blue door. Which will you choose?").lower()
        if (door_choice == "red"):
            print ("It was a trap door and you've fallen into Bowser's dungeon.")
        elif (door_choice == "blue"):
            print ("A high level minion waits behind this door and instantly kills you.")
        elif (door_choice == "yellow"):
            print ("You saved the princess!")
        else:
            print ("That isn't a valid door. You died anyways though.")

