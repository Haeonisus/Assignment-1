import random

Win = 0
Lose = 0
Tie = 0
game = True

print("Welcome to the game of Rock, Paper, Scissors.\n")

while True:
    computer_choice = random.choice(['rock', 'paper', 'scissors'])
    user_choice = input(
        "Choose rock, paper, or scissors: ").lower()
    if user_choice == 'rock':
        if computer_choice == 'rock':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, It's a tie!")
            Tie += 1
        elif computer_choice == 'paper':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You lose!")
            Lose += 1
        else:
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You win!")
            Win += 1
    elif user_choice == 'paper':
        if computer_choice == 'rock':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You win!")
            Win += 1
        elif computer_choice == 'paper':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, It's a tie!")
            Tie += 1
        else:
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You lose!")
            Lose += 1
    elif user_choice == 'scissors':
        if computer_choice == 'rock':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You lose!")
            Lose += 1
        elif computer_choice == 'paper':
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, You win!")
            Win += 1
        else:
            print(f"User choice is {user_choice}, Computer choice = {computer_choice}. So, It's a tie!")
            Tie += 1
    else:
        user_choice = input("Choose rock, paper, or scissors: ").lower()

    game_again = input('\nDo you want to play again? Answer (y/n): ').lower()
    if game_again == 'y':
        continue

    elif game_again == 'n':
        print(f'You won {Win} times, lost {Lose} times and tied {Tie} times.')
        print('Thank you for playing!')
        game = False
        break
    
    else:
        print('Invalid input. Please enter y or n.')
        game_again = input('\nDo you want to play again? Answer (y/n): ').lower()
