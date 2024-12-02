# Rock Paper Scissors version 01
# Tommy H. Yeargin, Jr.
# 2 December 2024

import random

class computer_move:
    def __init__(self):
        self.move = random.choice(['rock', 'paper', 'scissors'])

john = computer_move()

print("""Welcome to rock paper scissors (versus "John")!\n
Make a choice:
1. rock
2. paper
3. scissors\n""")
you = input("Enter your choice: ")
print(f"\nJohn's choice: {john.move}\n")

if you == john.move:
    print("It's a tie!")
elif you == 'rock' and john.move == 'scissors':
    print("You win!")
elif you == 'paper' and john.move == 'rock':
    print("You win!")
elif you == 'scissors' and john.move == 'paper':
    print("You win!")
elif you == 'rock' and john.move == 'paper':
    print("You lose!")
elif you == 'paper' and john.move == 'scissors':
    print("You lose!")
elif you == 'scissors' and john.move == 'rock':
    print("You lose!")
else:
    print("Invalid choice!")



