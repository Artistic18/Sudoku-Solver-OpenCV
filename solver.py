def find_empty(sudoku, pos):
    for i in range(9):
        for j in range(9):
            if sudoku[i][j] == 0:
                pos[0] = i
                pos[1] = j
                return True
    return False

def possible(sudoku,row,col,n):
    for i in range(9):
        if sudoku[row][i] == n:
            return False
    for i in range(9):
        if sudoku[i][col] == n:
            return False
    row0 = (row // 3) * 3
    col0 = (col //3 ) * 3
    for i in range(3):
        for j in range(3):
            if sudoku[row0+i][col0+j] == n:
                return False
    return True

def solve_sudoku(sudoku):
    pos =[0,0]
    if not find_empty(sudoku, pos):
        return True
    row = pos[0]
    col = pos[1]
    for num in range(1,10):
        if possible(sudoku,row,col,num):
            sudoku[row][col] = num
            if solve_sudoku(sudoku):
                return True
            sudoku[row][col] = 0
    return False

def solve(sudoku):
    if solve_sudoku(sudoku):
        return sudoku, 1
    else:
        return sudoku, 0
        
    
            