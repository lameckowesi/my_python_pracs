import random

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
# store the options in a list
options = [rock, paper, scissors]

# take input from the user 
your_input = int(input("Please choose 0 for rock, 1 for paper or 2 for scissors: "))

# assign user an option based on the input entered
your_choice = options[your_input]

# computer random option
computer_choice = random.choice(options)

# show user what they chose vs what the computer chose
print (f"You chose {your_choice} and the computer chose {computer_choice}") 

# check if user entered wrong number
if your_input >=3:
    print("You entered an invalid number")

# logic to tell if you win or lose 
elif your_choice == rock and computer_choice == scissors:
    print("You win")
elif your_choice == paper and computer_choice ==rock:
    print("You win")
elif your_choice ==scissors and computer_choice == paper:
    print("You win")
elif your_choice == computer_choice:
    print ("It is a draw")
else:
    print ("You lose")
    
