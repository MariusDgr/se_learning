def rotate(self, matrix):
    l, r = 0, len(matrix) - 1
    while l < r:
        for i in range(r - l):
            top, bottom = l, r
            
            # save topleft value
            top_left = matrix[top][l+i]

            # move bottom left to top left
            matrix[top][l+i] = matrix[bottom - i][l]

            # move bottom right into bottom left
            matrix[bottom - i][l] = matrix[bottom][r - i]

            # move top right to bottom right
            matrix[bottom][r-i] = matrix[top + i][r]

            # move top left to rop right
            matrix[top + i][r] = top_left

        r -= 1
        l += 1

