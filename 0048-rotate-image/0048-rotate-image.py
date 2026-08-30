class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
   

        for row in range(n):
            for col in range(row):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for row in matrix:
            left = 0
            right = n - 1

            while left < right:

                row[left],row[right] = row[right],row[left]
                left += 1
                right -= 1
            



