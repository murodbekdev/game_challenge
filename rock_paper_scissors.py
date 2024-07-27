import random

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)


'''

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

game_images = [rock, paper, scissors]  

user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")) # here indicating int as i escape the error called Index 

print(game_images[user_choice])   # here i can easily call the proper emoji once user chose the number

computer_choice = random.randint(0, 2)   # here i can use random module with randint method that returns a random number between the given range

print("Computer chose: ")

print(game_images[computer_choice])  # and here via computer choice, indicating the game_images's list 

if user_choice >=3 or user_choice < 0:
    print("You typed an invalid number, you lose!")    # if here user choice is greater than range of index, it will be indicated an invalid number and i lost
elif user_choice == 0 and computer_choice == 2:
    print("You win!")
elif computer_choice == 0 and user_choice == 2:   # here rock wins scissors
    print("You lose!")
elif computer_choice > user_choice:
    print("You lose!")
elif user_choice > computer_choice:    
    print("You win!")
elif computer_choice == user_choice:    # once me and compuer chose the same number it would be a draw
    print("It is a draw")

