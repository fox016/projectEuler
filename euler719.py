import math
from functools import reduce

def get_squares(start=16, end=10001):
    base = math.floor(math.sqrt(start))
    square = base**2
    squares = {}
    while square < end:
        squares[base] = square
        base+=1
        square = base**2
    return squares

def is_s_num(square, base):
    if square < 10:
        return False
    return s_num_helper("", str(square), base)

def s_num_helper(so_far, remaining, base):
    if remaining == "":
        if sum(map(int, so_far.split(" "))) == base:
            print(so_far, base)
            return True
        return False
    next_char = remaining[0]
    remaining = remaining[1:]
    if so_far != "":
        if s_num_helper(so_far + " " + next_char, remaining, base):
            return True
    return s_num_helper(so_far + next_char, remaining, base)


squares = get_squares(16, 10**12+1)
print(reduce(lambda y, z: squares[y] + squares[z], list(filter(lambda x: is_s_num(squares[x], x), squares.keys())), 1))
