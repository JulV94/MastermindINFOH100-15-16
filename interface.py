def print_msg_start():
    # Message M1
    """
    Affiche le message de début de partie.
    """
    print("\n----< Nouvelle partie >----\n")


def print_msg_wrong_entry():
    # Message M2
    """
    Affiche le message que la combinaison n'est pas valide.
    """
    print(20*" " + "Cette combinaison n'est pas valide.")


def print_msg_eval_entry(well_placed, good_colour):
    # Message M3
    """
    Affiche le nombre de pions biens placés [well_placed] et le
    nombre de pions de bonne couleur [good_colour].
    """
    print(20*" " + str(well_placed) + " pion(s) en place et " + str(good_colour) + " bonne(s) couleur(s).")


def print_msg_game_won(count):
    # Message M4
    """
    Affiche que la partie a été gagnée en [count] coups.
    """
    print(20*" " + "Bravo! Vous avez remporté la partie en " + str(count) + " coups.")


def print_msg_game_lost(code):
    # Message M5
    """
    Affiche qua la partie a été perdue ainsi que le [code] qui était à trouver.
    """
    code_str = "".join(code)
    print(20*" " + "Vous avez perdu la partie. La combinaison à trouver était: " + code_str + ".")


def input_prompt_entry(count):
    # Question Q1
    """
    Demande à l'utilisateur d'introduire sa combinaison pour le [count]-ième coup.
    """
    return input(str(count) + "/10 >>> ")


def input_continue_playing():
    # Question Q2
    """
    Demande à l'utilisateur s'il veut continuer à jouer ou quitter le programme.
    """
    return input("\nVoulez-vous [C]ontinuer à jouer ou [Q]uitter? ")