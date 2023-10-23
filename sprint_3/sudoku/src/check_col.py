def check_col(sudoku):

    i = 0 
    while i < len(sudoku):
        col = [row[i] for row in sudoku]
        for item in col:
            if col.count(item) > 1:
                return False
        i += 1
    return True

if __name__ == '__main__':
    
    import sys
    sys.path.append('..')

    import tests.sudoku_tests as test_cases


    for attr in sorted(test_cases.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, ':',check_col(test_cases.__dict__[attr]))