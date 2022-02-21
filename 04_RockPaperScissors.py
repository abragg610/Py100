rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
computer_choice = random.randint(0,2)

if (player_choice == 0 and computer_choice == 0):
    print (f"Your choice: \n {rock} \nComputer choice: \n {rock} \n You tie.")
elif (player_choice == 0 and computer_choice == 1):
    print (f"Your choice: \n {rock} \nComputer choice: \n {paper} \n You lose.")
elif (player_choice == 0 and computer_choice == 2):
    print (f"Your choice: \n {rock} \nComputer choice: \n {scissors} \n You win!")
elif (player_choice == 1 and computer_choice == 0):
    print (f"Your choice: \n {paper} \nComputer choice: \n {rock} \n You win!")
elif (player_choice == 1 and computer_choice == 1):
    print (f"Your choice: \n {paper} \nComputer choice: \n {paper} \n You tie.")
elif (player_choice == 1 and computer_choice == 2):
    print (f"Your choice: \n {paper} \nComputer choice: \n {scissors} \n You lose.")
elif (player_choice == 2 and computer_choice == 0):
    print (f"Your choice: \n {scissors} \nComputer choice: \n {rock} \n You lose")
elif (player_choice == 2 and computer_choice == 1):
    print (f"Your choice: \n {scissors} \nComputer choice: \n {paper} \n You win!")
elif (player_choice == 2 and computer_choice == 2):
    print (f"Your choice: \n {scissors} \nComputer choice: \n {scissors} \n You tie.")
else:
    print ("You shouldn't be reading this.")


