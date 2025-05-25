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
        print(f"[{row},{col}]", end="")
    print()

def generate_movements(size):
    choices = []
    mov = []
    for a in range(size):
        for b in range(size):
            mov = [a, b]
            choices.append(mov)
    return choices

print_board(generate_movements(3))
# positions_example = generate_placements(5)
# print_board(positions_example)
# print_board(column_comb())


