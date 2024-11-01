import random
welcome = "This is 'Rock, Paper, Scissors' game."
print (welcome.center(75))
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
---'    ____)____
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
your_choice = int(input("1 for Rock\n2 for Paper\n3 for Scissors.\nEnter your choice: "))

images = [rock, paper, scissors]
if(your_choice < 4):
    print(images[your_choice-1])

computer_choice = random.randint(1, 3)
if(your_choice < 4):
    print("Computer choose: ")
if(your_choice < 4):
    print(images[computer_choice-1])

if (your_choice > 3):
    print("Invalid Number. You Lose 😝😝.")
elif (your_choice == computer_choice):
    print("Match Draw. 😝😝")
elif (your_choice == 1 and computer_choice == 2):
    print("You lose. 😂😂 😝😝")
elif (your_choice == 1 and computer_choice == 3):
    print("You win. Well nothing impressive.")
elif (your_choice == 2 and computer_choice == 1):
    print("You win. Well nothing impressive.")
elif (your_choice == 2 and computer_choice == 3):
    print("You lose. 😂😂 😝😝")
elif (your_choice == 3 and computer_choice == 1):
    print("You lose. 😂😂 😝😝")
else:
    print("You win. Well nothing impressive.")