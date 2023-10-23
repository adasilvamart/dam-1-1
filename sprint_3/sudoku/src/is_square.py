
def is_square(sudoku):
    for row in sudoku:
        if len(row) != len(sudoku):
            return False
    return True

if __name__ == '__main__':
    
    import sys
    sys.path.append('..')

    import tests.sudoku_tests as test_cases


    for attr in sorted(test_cases.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, ':', is_square(test_cases.__dict__[attr]))