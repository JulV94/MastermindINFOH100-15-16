from random import sample

VALID_COLORS = ['r', 'j', 'v', 'b', 'o', 'c', 't', 'f']
PATTERN_LENGTH = 4


def random_code():
    return sample(VALID_COLORS, 4)


def is_valid_pattern(pattern):
    result = len(pattern) == PATTERN_LENGTH
    i = 0
    while i < PATTERN_LENGTH and result:
        result = pattern[i] in VALID_COLORS
        i += 1
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
    return well_placed, good_color
