#!/usr/bin/python3

from sys import argv

# board_size = 0
# result = []

# if (len(argv) != 2):
#     print("Usage: nqueens N")
#     exit(1)
# try:
#     board_size = int(argv[1])
# except Exception as error:
#     print(error)

# print(f"Board Size: {board_size}")




# def test_board(size: int = 0) -> list:


# def generate_placements(size) -> list:
#     positions = []
#     for a in range(size):
#         for b in range(size):
#             mov = []
#             mov.append(a)
#             mov.append(b)
#             positions.append(mov)
#     return positions


def print_board(board: list):
    current_row = board[0][0]
    for coord in board:
        row, col = coord
        if row != current_row:
            print()
            current_row = row
        print(f" [{row}, {col}]", end="")
    print()

# this is the straightforward one.
# def generate_movements(size):
#     choices = []
#     mov = []
#     for a in range(size):
#         for b in range(size):
#             mov = [a, b]
#             choices.append(mov)
#     return choices

def make_permutations(numbers, used, current, all_perms):
    if len(current) == len(numbers):
        all_perms.append(current)
        return
    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            current.append(numbers[i])
            make_permutations(numbers, used, current, all_perms)
            current.pop()

def convert_to_positions(column_list):
    positions = []
    for row in range(len(column_list)):
        col = column_list[row]
        positions.append([row, col])
    return positions

def check_diagonals(positions):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            row1, col1 = positions[i]
            row2, col2 = positions[j]
            if row1 - row2 == col1 - col2:
                return False
    return True

def solve_n_queens(n):
    numbers = []
    for i in range(n):
        numbers.append(i)
    all_perms = []
    used = []
    for i in range(n):
        used.append(False)
    make_permutations(numbers, used, [], all_perms)
    solutions = []
    for perm in all_perms:
        pos = convert_to_positions(perm)
        if check_diagonals(pos):
            solutions.append(pos)
    # MISTAKE: Not returning anything
    print(f"Found {len(solutions)} solutions")

def solve_n_queens_more_mistakes(n):
    numbers = list(range(n))
    all_perms = []
    used = [False] * n
    
    make_permutations(numbers, used, [], all_perms)
    
    solutions = []
    for perm in all_perms:
        pos = convert_to_positions(perm)
        if check_diagonal(pos):
            solutions.append(pos)
    
    return solutions

def check_diagonal(positions, n):
    for i in range(len(positions)):
        for j in range(i, len(positions)):
            row1, col1 = positions[i]
            row2, col2 = positions[j]
            if abs(row1 - row2) == abs(col1 - col2):
                return False
    return True

def make_permutations_broken(numbers, used, current, all_perms):
    if len(current) >= len(numbers):
        all_perms.append(current[:])
        return
    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            current.append(numbers[i])
            make_permutations_broken(numbers, used, current, all_perms)
            current.pop()
            used[i] = False

# print_board(generate_movements(5))
# print(choices_to_positions(generate_choices(4)))
# positions_example = generate_placements(5)
# print_board(positions_example)
# print_board(column_comb())


