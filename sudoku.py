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
        for n in range(9):
            board_square[n] = random.choice(available_num)
            available_num.remove(board_square[n])
        full_board[square] = board_square
        print(board_square)
    print(full_board)

# wyświetlanie planszy do zmiany (powiązać indexy żeby wyśwetlało wszystko po kolei)
def display_board():
    row_list = []
    i = 0
    j = 0
    for x in range(9):
        row_list.append(full_board[i][j])
        j = j + 1
        if j % 3 == 0:
            i = i + 1
            j = 0
    row = ' | '.join(row_list)
    print('| '+ row )


square_filling()
display_board()