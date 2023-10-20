def check_row(sudoku):
    for row in sudoku:
        for item in row:
            if row.count(item) > 1:
                return False
    return True

def check_col(sudoku):
    i = 0
    while i < len(sudoku):
        col = [row[i] for row in sudoku]
        for item in col:
            if col.count(item) > 1:
                return False
        i += 1
    return True

def check_valid(sudoku):
    for row in sudoku:
        for item in row:
            if not isinstance(item, int) or max(row) > len(sudoku):
                return False
    return True

def check_sudoku(sudoku):
    return check_valid(sudoku) and check_col(sudoku) and check_row(sudoku)
        

correct = [[1,2,3],
           [2,3,1],
           [3,1,2]]
incorrect3 = [[1,2,3,4,5],[2,3,1,5,6],[4,5,2,1,3],[3,4,5,2,1],[5,6,4,3,2]]
incorrect4 = [['a','b','c'],['b','c','a'],['c','a','b']]


incorrect = [[1,2,3,4],
             [2,3,1,3],
             [2,1,2,3],
             [4,4,4,4]]


print(check_sudoku(correct))
print(check_sudoku(incorrect))
print(check_valid(incorrect4))