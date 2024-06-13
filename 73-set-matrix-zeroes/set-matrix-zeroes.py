class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        arr=[]
        brr=[]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if matrix[i][j]==0:
                    arr.append(i)
                    brr.append(j)
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if i in arr or j in brr:
                    matrix[i][j]=0
        return matrix
                