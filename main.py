def find_next_empty(puzzle):
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return None, None#if no spaces in the puzzle are empty(-1)

def is_valid(puzzle, guess, row, col):
    # figures out whether the guess at of the puzzle is valid guess
    # returns True if is valid, False otherwise
    # the row:
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    # we want where the 3x3 square statrs
    # and iterate over the 3
    row_start = (row // 3) * 3# we want it to be intger
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle [r][c] == guess:
                return False



def solve_sudoku(puzzle):
    row, col = find_next_empty(puzzle)
    # step 2: if there's nowhere left, then we're done beacause we only allowed valid inputs
    if row is None:
        return True

    # step 3: if there's a plave to put a number, then make a guess between 1 and 9
    for guess in range(1, 10):
    # step 4:check if this is a valid guess
        if is_valid(puzzle, guess, row, col):
    # step 5: if it's valid,then place that guess
           puzzle [row][col] = guess
    # now recurse using this puzle
    #step 6:recursively call our function
           if solve_sudoku(puzzle):
              return True
    #step 7: if does not solve the puzzle
    #try new number
        puzzle[row][col] = -1
    # step 8:if none of it work then it's unsolvable
    return False
if __name__ == '__main__':
    example_board = [
        [3, 9, -1,   -1, 5, -1,   -1, -1, -1],
        [-1, -1, -1,   2, -1, -1,   -1, -1, 5],
        [-1, -1, -1,   7, 1, 9,   -1, 8, -1],

        [-1, 5, -1,   -1, 6, 8,   -1, -1, -1],
        [2, -1, 6,   -1, -1, 3,   -1, -1, -1],
        [-1, -1, -1,   -1, -1, -1,   -1, -1, 4],

        [5, -1, -1,   -1, -1, -1,   -1, -1, -1],
        [6, 7, -1,   1, -1, 5,   -1, 4, -1],
        [1, -1, 9,   -1, -1, -1,   2, -1, -1]
    ]
    print(solve_sudoku(example_board))
    print(example_board)