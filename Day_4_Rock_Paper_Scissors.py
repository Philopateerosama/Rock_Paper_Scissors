import random
Rock ="""
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
"""

Paper ="""
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)
"""

scissor ="""
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
list_of_images = [Rock , Paper , scissor]

user_num = int(input("what do you chosse? Type 0 for Rock , 1 for Paper or 2 for Scissor\n"))
if user_num <=2 or user_num >=0:
    print(list_of_images[user_num])

com_num = random.randint(0 , 2)
print(f"computer chose:")
print(list_of_images[com_num])

if user_num == 0 and com_num == 2:
    print("You win!")
elif user_num == 2 and com_num == 0:
    print("You lose!")
elif user_num == 2 and com_num == 1:
    print("You win!")
elif com_num > user_num:
    print("You lose!")
elif user_num == 1 and com_num == 0:
    print("You win!")
elif com_num == user_num:
    print("It's a draw!")
elif user_num > 2 or user_num <0:
    print("you typed an invalid number . You lose!")
