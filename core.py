from random import sample

VALID_COLORS = ['r', 'j', 'v', 'b', 'o', 'c', 't', 'f']


def random_code():
    return sample(VALID_COLORS, 4)


def is_valid_pattern(pattern):  # Ugly code but we have to put only one return
    result = True
    if len(pattern) != 4:
        result = False
    for elem in pattern:
        if elem not in VALID_COLORS:
            result = False
    return result


def try_pattern(pattern, code):
    well_placed = 0
    good_color = 0
    for i in range(len(code)):
        # Do it the other way around in order to guarantee unicity
        if code[i] == pattern[i]:
            well_placed += 1
        elif code[i] in pattern:
            # if code[i] is twice in pattern, this still returns 1
            # This doesn't run if code[i] is well_placed => no overcount issues
            good_color += 1
        # This works and is beautiful!
        # pop is a bad idea altogether because it modifies code
    return (well_placed, good_color)
