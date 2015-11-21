from interface import *
from core import *

MAX_ATTEMPTS = 10


def play():
    play_again = True
    while play_again:
        print_msg_start()   # Should be in game() but we have the 15 lines limitation
        game()
        entry = ''
        while entry not in 'cq':
            entry = input_continue_playing().lower().strip()
        play_again = entry == c


def game():
    attempts = 1
    code = random_code()
    is_won = False
    while attempts <= 10 and not is_won:
        pattern = list(input_prompt_entry(attempts).lower())
        if is_valid_pattern(pattern):
            result = try_pattern(pattern, code)
            print_msg_eval_entry(result[0], result[1])
            if result[0] == 4:
                is_won = True
            else:
                attempts += 1
        else:
            print_msg_wrong_entry()
    print_msg_game_won(attempts) if is_won else print_msg_game_lost(code)


if __name__ == "__main__":  # If it's not a module, if it's called (main)
    play()  # Launch the game
