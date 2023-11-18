# ASCII art representations of Rock, Paper, and Scissors
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

import random

# User input to choose rock (0), paper (1), or scissors (2)
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

# Computer's choice stored in a list
computer_pick = [rock, paper, scissors]

# User's choice based on input
user_choice = computer_pick[user_pick]
print(user_choice)

# Computer randomly selects a choice from the given options then prints it
num_computer_pick = len(computer_pick)
computer_choice = random.randint(0, num_computer_pick - 1)
selected_pick = computer_pick[computer_choice]
print(f"Computer chose:\n {selected_pick}")

# Define rules for the rock, paper, scissors game
game_rules = rock > scissors or rock < paper or paper > rock or paper < scissors or scissors > paper or scissors < rock

# Compare user's and computer's selection to determine the result
if user_choice > selected_pick:
  print("You win!")
elif user_choice < selected_pick:
  print("You lose!")
elif user_choice == selected_pick:
  print("Draw!")
