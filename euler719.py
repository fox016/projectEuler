import math

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
    perms = get_digit_permutations(square)
    for perm in perms:
        if sum(perm) == base:
            print(square, perm, base)
            return True
    return False

def get_digit_permutations(num):
    digits = str(num)
    solution = []
    perm_helper("", digits, solution)
    return list(map(lambda x: list(map(int, x.split(" "))), solution))[:-1]

def perm_helper(so_far, remaining, solution):
    if remaining == "":
        solution.append(so_far)
        return
    next_char = remaining[0]
    remaining = remaining[1:]
    if so_far != "":
        perm_helper(so_far + " " + next_char, remaining, solution)
    perm_helper(so_far + next_char, remaining, solution)

total = 0
squares = get_squares(16, 10**12+1)
for base in squares:
    if is_s_num(squares[base], base):
        total += squares[base]
print(total)
