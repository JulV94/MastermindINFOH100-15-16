from interface import *
from core import *


def play():
    play_again = True
    while play_again:
        game()
        if input_continue_playing().lower() != 'c':
            play_again = False


def game():
    print_msg_start()
    attempts = 1
    code = random_code()
    is_won = False
    while attempts <= 10 and not is_won:
        pattern = input_prompt_entry(attempts)
        if is_valid_pattern(pattern):
            result = try_pattern(pattern, code)
            print_msg_eval_entry(result[0], result[1])
            if result[0] == 4:
                is_won = True
            else:
                attempts += 1
        else:
            print_msg_wrong_entry()
    if is_won:
        print_msg_game_won(attempts)
    else:
        print_msg_game_lost(code)

if __name__ == "__main__":  # If it's not a module, if it's called (main)
    play()  # Launch the game
