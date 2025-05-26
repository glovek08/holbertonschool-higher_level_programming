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

def generate_queen_moves(numbers, used, current, all_perms):
    if len(current) == len(numbers):
        all_perms.append(current[:])
        return
    for i in range(len(numbers)):
        if not used[i]:
            used[i] = True
            current.append(numbers[i])
            generate_queen_moves(numbers, used, current, all_perms)
            current.pop()
            used[i] = False

def to_holberton_format(column_list):
    return [[row, col] for row, col in enumerate(column_list)]

def check_diagonals(positions):
    for i in range(len(positions)):
        for j in range(i + 1, len(positions)):
            row1, col1 = positions[i]
            row2, col2 = positions[j]
            if abs(row1 - row2) == abs(col1 - col2):
                return False
    return True

def solve_n_queens(n):
    numbers = list(range(n))
    all_perms = []
    used = [False] * n
    generate_queen_moves(numbers, used, [], all_perms)
    solutions = []
    for perm in all_perms:
        pos = to_holberton_format(perm)
        if check_diagonals(pos):
            solutions.append(pos)
    return solutions


# print_board(generate_movements(5))
# print(choices_to_positions(generate_choices(4)))
# positions_example = generate_placements(5)
# print_board(positions_example)
# print_board(column_comb())


