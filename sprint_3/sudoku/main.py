from src.check_sudoku import check_sudoku
import tests.sudoku_tests as test_cases

for test in sorted(test_cases.__dict__):
    if test.startswith('__'):
        pass
    else:
        print(test, ':', check_sudoku(test_cases.__dict__[test]))