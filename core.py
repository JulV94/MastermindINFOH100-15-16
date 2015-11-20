from random import sample, seed


def random_code():
    seed()
    return sample(['r', 'j', 'v', 'b', 'o', 'c', 't', 'f'], 4)



def is_valid_pattern(pattern):  # Ugly code but we have to put only one return -_-
    result = True
    valid_colors = ['r', 'j', 'v', 'b', 'o', 'c', 't', 'f']
    if len(pattern) != 4:
        result = False
    for elem in pattern:
        if elem not in valid_colors:
            result = False
    return result


def try_pattern(pattern, code):
    well_placed = 0
    good_color = 0
    for i in range(len(pattern)-1, -1, -1):
        if pattern[i] == code[i]:
            well_placed += 1
            pattern.pop(i)
            code.pop(i)

    for elem in pattern:
        if elem in code:
            good_color += 1

    return tuple(well_placed, good_color)
