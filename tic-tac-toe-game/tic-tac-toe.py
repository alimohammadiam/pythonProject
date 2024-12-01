from termcolor import colored

board = list(range(1, 10))
winners = ((0, 1, 2,), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))
moves = ((1, 3, 7, 9), (5,), (2, 4, 6, 8))


def print_board():
    j = 1
    for i in board:
        end = '  '
        if j % 3 == 0:
            end = '\n'
        if i == 'X':
            print(colored(f'[{i}]', 'red'), end=end)
        elif i == 'O':
            print(colored(f'[{i}]', 'blue'), end=end)
        else:
            print(f'[{i}]', end=end)
        j += 1


def make_move(brd, plyr, mve, undo=False):
    if can_move(brd, mve):
        brd[mve-1] = plyr
        win = is_winner(brd, plyr)
        if undo:
            brd[mve-1] = mve
        return True, win
    return False, False


def can_move(brd, mve):
    if mve in range(1, 10) and isinstance(brd[mve-1], int):
        return True
    return False


def is_winner(brd, plyr):
    win = True
    for tup in winners:
        win = True
        for j in tup:
            if brd[j] != plyr:
                win = False
                break
        if win:
            break
    return win


def has_empty_space():
    return board.count('X') + board.count('O') != 9


def computer_move():
    mv = -1
    # computer can win ?
    for i in range(1, 10):
        if make_move(board, computer, i, True)[1]:
            mv = i
            break

    # Player can win ?
    if mv == -1:
        for i in range(1, 10):
            if make_move(board, player, i, True)[1]:
                mv = i
                break

    # mov
    if mv == -1:
        for tup in moves:
            for i in tup:
                if can_move(board, i):
                    mv = i
                    break
            if mv != -1:
                break

    return make_move(board, computer, mv)


player, computer = 'X', 'O'
print('Player: [X]\nComputer: [O]\n')

while has_empty_space():
    print_board()
    move = int(input('Enter your move (1-9): '))
    moved, won = make_move(board, player, move)
    if not moved:
        print('Invalid number! Try again!')
        continue
    if won:
        print(colored('You are Won', 'green'))
        break
    elif computer_move()[1]:
        print(colored('You are lose!', 'yellow'))
        break

print_board()
