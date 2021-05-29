
def makeGrid(nRows, nCols):
    grid = [['empty']*nCols for _ in range(nRows)]
    return grid


def play(grid, column, checker):

    if 0 > column or column > len(grid):
        return False

    if grid[0][column] != 'empty':
        return False

    for row in grid[::-1]:
        if row[column] == 'empty':
            row[column] = checker
            return True

    return False


def win(grid, column):
    if column > len(grid) + 1:
        return 'empty'
    
    user = 'red'
    if (check_won(grid, user, column) or
            check_won(zip(*grid), user, column) or
            diagcheck_won(grid, user, column) or
            diagcheck_won(grid[::-1], user, column)):
        return user

    return 'empty'


def check_won(grid, user, column):
    return any(condition_met(cell == user for cell in row) for row in grid)


def diagcheck_won(grid, user, column):
    return condition_met(grid[x][x] == user for x in range(column))

def condition_met(items):
    return list(items).count(True) >=4


def toString(grid):
    table = ''
    for i, row in enumerate(grid):
        table += '|'
        for cell in row:
            if cell == 'red':
                table += 'X'
            elif cell == 'black':
                table += 'O'
            else:
                table += ' '
        table += f'|{i}\n'
    table += '+' + '-' * len(grid[0]) + '+'
    return table
