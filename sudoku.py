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
                i = i + 1
                j = j - 3
            row = ' | '.join(row_list)
            print( row )

def verification_row():
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
                i = i + 1
                j = j - 3
            for elem in row_list:
                if row_list.count(elem) > 1:
                    print("Wiersz nie spełnia założeń gry w sudoku:")
                    print(row_list)
                    action()

def verification_column():
    i = 0
    j = 0
    for w in range(3):
        for x in  range(3):
            column_list = []
            for y in range(3):
                if y == 0:
                    i = w
                    j = x
                for z in range(3):
                    column_list.append(full_board[i][j])
                    j = j + 3
                i = i + 3
                j = j - 9
            for elem in column_list:
                if column_list.count(elem) > 1:
                    print("Kolumna nie spełnia założeń gry w sudoku:")
                    print(column_list)
                    action()


def action():
    print('''
    1 - generuj sudoku
    2 - sprawdź czy kolumny spełniają założenia gry
    3 - sprawdź czy wiersze spełniają założenia gry
    4 - zakończ
    ''')
    x = input('Określ akcję: ')

    if x == '1':
        return square_filling(), display_board(), action()
    elif x == '2':
        try:
            return verification_column()
        except:
            print('Nie wygenerowano wcześniej sudoku')
            return action()
    elif x == '3':
        try:
            return verification_row()
        except:
            print('Nie wygenerowano wcześniej sudoku')
            return action()
    elif x == '4':
        return quit()
    else:
        print('błędne polcenie')
        return action()

action()