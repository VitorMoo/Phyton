import module_random_number

start_range = 1
end_range = 100
max_guesses = 6

def play_game():
    target_number = module_random_number.generate_random(start_range, end_range)
    print("Guess a number between 1 and 100\n")

    number_of_guesses = 0

    while True:
        number_of_guesses += 1
        guess = int(input(f'Guess #{number_of_guesses}: '))

        if guess > target_number:
            print('\nToo high, try again\n')
        elif guess < target_number:
            print('\nToo low, try again\n')
        else:
            print('Correct!')
            print(f'Congratulations! You won in {number_of_guesses} guesses.')
            break

        if number_of_guesses >= max_guesses:
            print(f"Sorry, you didn't guess in time. The correct answer was {target_number}.")
            break

def main():
    play_game()

main()
