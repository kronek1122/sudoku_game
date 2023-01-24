import random
import copy

board_square = ['-','-','-',
                '-','-','-',
                '-','-','-',]

full_board = [[],[],[],
            [],[],[],
            [],[],[],]

num = ['1','2','3','4','5','6','7','8','9']

def square_filling():
    for square in range(9):
        available_num = copy.deepcopy(num)
        board_square_copy = copy.deepcopy(board_square)
        for n in range(9):
            board_square_copy[n] = random.choice(available_num)
            available_num.remove(board_square_copy[n])
        full_board[square] = board_square_copy

def display_board():
    i = 0
    j = 0
    for w in range(3):
        for x in  range(3):
            row_list = []
            for y in range(3):
                if y == 0:
                    i = 3 * w
                    j = x * 3
                for z in range(3):
                    row_list.append(full_board[i][j])
                    j = j + 1
                if z == 2:
                    i = i + 1
                j = j - 3
            row = ' | '.join(row_list)
            print( row )

# dodać sprawdzenie poprawności kolumn i wierszy
def verification_columns():
    pass



square_filling()
display_board()
