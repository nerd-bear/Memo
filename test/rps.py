import random
import Levenshtein

Choices = ['rock', 'paper', 'scissors']

while True:
    user_choice = input("Enter your choice (rock, paper, scissors): ").lower().strip()

    for choice in Choices:
        if Levenshtein.ratio(user_choice.lower(), choice) * 100 >= 40:
            user_choice = choice

    computer_choice = random.choice(Choices)
    
    if user_choice not in Choices:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        continue
    
    if user_choice == computer_choice:
        print(f"It's a tie! Both chose {user_choice}!")
        continue
    
    if (user_choice == 'rock' and computer_choice == 'scissors') or \
       (user_choice == 'scissors' and computer_choice == 'paper') or \
       (user_choice == 'paper' and computer_choice == 'rock'):
        print(f"You win! {user_choice} beats {computer_choice}.")
    else:
        print(f"Computer wins! {computer_choice} beats {user_choice}.")
    break


import random,Levenshtein
c=['rock','paper','scissors']
while 1:
    u=input("Enter your choice (rock, paper, scissors): ").lower().strip()
    for i in c:
        if Levenshtein.ratio(u.lower(),i)*100>=40:u=i
    d=random.choice(c)
    if u not in c:print("Invalid choice. Please enter rock, paper, or scissors.");continue
    if u==d:print(f"It's a tie! Both chose {u}!");continue
    if(u=='rock'and d=='scissors')or(u=='scissors'and d=='paper')or(u=='paper'and d=='rock'):print(f"You win! {u} beats {d}.")
    else:print(f"Computer wins! {d} beats {u}.")
    break