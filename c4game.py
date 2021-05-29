from connect4 import *


def main(step=1, moves=0):
    valid_sizes = []
    while True:
        if step == 1:
            try:
                action = input(
                    'Please enter the size of the game you want to play: ')
                if action.lower() == 'quit':
                    print('Thanks for playing')
                    break
                user_sizes = action.split(',')
                if len(user_sizes) != 2:
                    raise ValueError
                for size in user_sizes:
                    valid_sizes.append(int(size))

            except ValueError:
                print('Invalid input or format. Format is rows,columns')
                step = 1
                continue

            nRows, nCols = valid_sizes
            grid = makeGrid(nRows, nCols)
            step = 2
            continue

        if step == 2:
            grid_is_full = True
            # Check if the grid is full
            for row in grid:
                for cell in row:
                    if cell == 'empty':
                        grid_is_full = False
                        break

            if grid_is_full:
                print('The game is a tie')
                step = 1
                continue
            else:
                step = 3
                continue

        if step == 3:
            action = input('Where does red (X) want to play? ')
            if action.lower() == 'quit':
                print('Thanks for playing')
                break
            red_move = int(action)
            if play(grid, red_move, 'red'):
                moves +=1
                print(toString(grid))
                if win(grid, red_move) == 'red':
                    print(f'Red wins the game after {moves} moves')
                    step = 1
                
                else:
                    step = 4
                
            else:
                print('That is not a valid move.')
                step = 3
            continue

        if step == 4:
            grid_is_full = True
            # Check if the grid is full
            for row in grid:
                for cell in row:
                    if cell == 'empty':
                        grid_is_full = False
                        break

            if grid_is_full:
                print('The game is a tie')
                step = 1
            else:
                step = 5
            continue
        if step == 5:
            action = input('Where does black (O) want to play? ')
            if action.lower() == 'quit':
                print('Thanks for playing')
                break
            black_move = int(action)
            if play(grid, black_move, 'black'):
                moves +=1
                
                print(toString(grid))
                if win(grid, black_move) == 'black':
                    print(f'Black wins the game after {moves} moves')
                    step = 1
                else:
                    step = 6

            else:
                print('That is not a valid move.')
                step = 5

            continue
        if step == 6:
            step = 2
            continue


if __name__ == '__main__':
    main()
