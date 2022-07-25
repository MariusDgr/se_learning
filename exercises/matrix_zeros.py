"leetcode 73"
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    ROWS, COLS = len(matrix), len(matrix[0])
    row_zero = False # extra val needed because of row / col overlap
    
    # find cols and rows with 0 and store in first col / row
    for r in range(ROWS):
        for c in range(COLS):
            if matrix[r][c] == 0:
                matrix[0][c] = 0
                    
                if r > 0: 
                    matrix[r][0] = 0
                else:
                    row_zero = True
                    
    print(ROWS, COLS)
    # fill matrix with 0
    for r in range(1, ROWS):
        for c in range(1, COLS):
            print(matrix[r][c], r, c)
            if matrix[0][c] == 0 or matrix[r][0] == 0:
                matrix[r][c] = 0
                
            
            
    # fill the indicator row/col with 0
    
    if matrix[0][0] == 0:
        for r in range(ROWS):
            matrix[r][0] = 0
            
    if row_zero: 
        for c in range(COLS):
            matrix[0][c] = 0