def check_row(a):
    for row in a:
        for item in row:
            if row.count(item) > 1:
                return False
    return True
def check_col(a):
    i = 0
    while i < len(a):
        col = [row[i] for row in a]
        for item in col:
            if col.count(item) > 1:
                return False
        i += 1
    return True
def check_sudoku(a):
    for row in a:
        for item in row:
            if not isinstance(item, int) or max(row) > len(a):
                return False
    return check_col(a) and check_row(a)

correct = [[1,2,3],[2,3,1],[3,1,2]]
incorrect = [[1,2,3,4],[2,3,1,3],[2,1,2,3],[4,4,4,4]]
incorrect2 = [[1,2,3,4],[2,3,1,4],[4,1,2,3],[3,4,1,2]]
incorrect3 = [[1,2,3,4,5],[2,3,1,5,6],[4,5,2,1,3],[3,4,5,2,1],[5,6,4,3,2]]
incorrect4 = [['a','b','c'],['b','c','a'],['c','a','b']]
incorrect5 = [ [1, 1.5],[1.5, 1]]

print(check_sudoku(incorrect4))