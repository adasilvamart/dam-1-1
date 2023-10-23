def check_row(a):
    for row in a:
        for item in row:
            if row.count(item) > 1:
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
            print(attr, ':', check_row(test_cases.__dict__[attr]))