import random
random_n = random.randint(1, 100)

print("Welcome to the game of UP and DOWN.")
count = 0

while True:
    user_input = int(input("Press a number to start this game: "))

    if user_input > 100 or user_input < 1:
        print("Please enter a number between 1 and 100")
    elif user_input > random_n:
        count += 1
        print(f"You game is {user_input} and it should be DOWN. Try again!")
    elif user_input < random_n:
        count += 1
        print(f"You game is {user_input} and it should be UP. Try again!")
    else:
        count += 1
        print(f'You got it! You guessed {count} times')
        play_again = input(
            '\nDo you want to play again? Answer with "yes" or "no": ').lower()
        if play_again == 'yes':
            print(f'\nSmallest amount of guesses of previous game: {count}')
            random_n = random.randint(1, 100)
            count = 0
            continue
        else:
            print('Thank you for playing!')
            break
    print('\n')
