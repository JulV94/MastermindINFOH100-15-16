from interface import *
from core import *

MAX_ATTEMPTS = 10


def play():
    play_again = True
    while play_again:
        game()
        entry = ''
        while entry not in 'cq':
            entry = input_continue_playing().lower().strip()
        play_again = entry == c


def round(code, attempts):
    pattern = sanitize(input_prompt_entry(attempts))
    while not is_valid_pattern(pattern):
        print_msg_wrong_entry()
        pattern = list(input_prompt_entry(attempts).lower())
    (well_placed, good_color) = try_pattern(pattern, code)
    print_msg_eval_entry(well_placed, good_color)
    return well_placed == 4


def init_game():
    attempts = 1
    code = random_code()
    is_won = False
    print_msg_start()
    return attempts, code, is_won


def end_game(is_won, attempts, code):
    if is_won:
        print_msg_game_won(attempts)
    else:
        print_msg_game_lost(code)


def game():
    attempts, code, is_won = init_game()
    while attempts <= MAX_ATTEMPTS and not is_won:
        is_won = round(code, attempts)
        attempts += 1
    end_game(is_won, attempts, code)


if __name__ == "__main__":  # If it's not a module, if it's called (main)
    play()  # Launch the game
