
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

print("Let's play rock, paper, scissors! ")
game = [rock, paper, scissors]
my_choice = int(input("Choose 0 for rock, 1 for paper and 2 for scissors \n"))

#if my_choice >= 0 and my_choice <=2: --> another solution
#    print(game[my_choice]) --> another solution

# my code
if my_choice == 0:
    print(rock)
elif my_choice == 1:
     print(paper)
elif my_choice == 2:
    print(scissors)
else:
    print("You typed an invalid number, You lose")
    exit()


computer_pick = [rock, paper, scissors]
computer_picks = random.randint(0,2)
print(f"The computer chose: {computer_pick[computer_picks]}")

combination = [my_choice, computer_picks]

if combination == [0, 1] or combination == [1, 2] or combination == [2, 0]:
   print("You lose")
elif combination == [0, 2] or combination == [1, 0] or combination == [2, 1]:
    print("You win")
elif combination == [0, 0] or combination == [1, 1] or combination == [2, 2]:
    print("It's a tie")



print('''
         /\     /\\
        {  `---'  }
        {  O   O  }
        ~~>  V  <~~
         \\\\ \|/ /
          `-----'____
          /     \\    \\_
         {       }\\  )_\\_   _
         |  \_/  |/ /  \\_\\_/ )
          \\__/  /(_/     \\__/
            (__/
''')

print("Thank you for playing! MEOW! ")

