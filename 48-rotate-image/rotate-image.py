class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Transpose the matrix
        matrix[:] = [list(row) for row in zip(*matrix)]
    
        # Reverse each row
        matrix[:] = [row[::-1] for row in matrix]
        

        