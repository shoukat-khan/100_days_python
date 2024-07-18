# import random

# random_integer = random.randint(1, 10)

# print(random_integer)

# random_float = random.random()

# print(random_float)


# #list data type

# fruits = ["Apple", "Orange", "Banana", "Grapes"]  

# for f in fruits:
#     print(f)

# #list inside list

# male = ["Ali", "Ahmed", "Shoukat"]
# female = ["Sara", "Ayesha", "Sana"]

# people = [male,female]


# print(people[0][1])



# 

#rock paper scissor game
import random

rock =""" 
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""


scissor="""" 
   _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)"""

paper="""   
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)"""


game_images = [rock, paper, scissor]

user_choice = int(input("What do you choose? Type \n0 for Rock, \n1 for Paper or \n2 for Scissors.\n"))

if user_choice >= 3 or user_choice < 0:
    print("You typed an invalid number, you lose!")
else:
    print(game_images[user_choice])

    computer_choice = random.randint(0, 2)
    print("Computer chose:")
    print(game_images[computer_choice])

    if user_choice == 0 and computer_choice == 2:
        print("You win!")
    elif computer_choice == 0 and user_choice == 2:
        print("You lose")
    elif computer_choice > user_choice:
        print("You lose")
    elif user_choice > computer_choice:
        print("You win!")
    elif computer_choice == user_choice:
        print("It's a draw")

         