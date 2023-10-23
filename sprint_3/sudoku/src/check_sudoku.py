import sys
sys.path.append('..')

from src.is_valid import is_valid
from src.is_square import is_square
from src.check_col import check_col
from src.check_row import check_row

def check_sudoku(sudoku):
    return is_valid(sudoku) and is_square(sudoku) and check_col(sudoku) and check_row(sudoku)

if __name__ == '__main__':
    
    import sys
    sys.path.append('..')

    import tests.sudoku_tests as test_cases


    for attr in sorted(test_cases.__dict__):
        if attr.startswith('__'):
            pass
        else:
            print(attr, ':', check_sudoku(test_cases.__dict__[attr]))