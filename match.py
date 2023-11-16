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
user_pick = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))

computer_pick = [rock, paper, scissors]
user_choice = computer_pick[user_pick]
print(user_choice)

num_computer_pick = len(computer_pick)
computer_choice = random.randint(0, num_computer_pick - 1)
selected_pick = computer_pick[computer_choice]
print(f"Computer chose:\n {selected_pick}")


game_rules = rock > scissors or rock < paper or paper > rock or paper < scissors or scissors > paper or scissors < rock

if user_choice > selected_pick:
  print("You win!")
elif user_choice < selected_pick:
  print("You lose!")
elif user_choice == selected_pick:
  print("Draw!")