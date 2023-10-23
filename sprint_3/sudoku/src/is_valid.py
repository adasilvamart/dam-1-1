def is_valid(sudoku):

    for row in sudoku:
        for num in row:
            if not isinstance(num, int) and num not in range(1, len(sudoku) -1):
                return False
            # else: cumple condiciones return True
    return True


if __name__ == '__main__':
    
    import sys
    sys.path.append('..')

    import tests.sudoku_tests as test_cases


    for attr in sorted(test_cases.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, ':', is_valid(test_cases.__dict__[attr]))