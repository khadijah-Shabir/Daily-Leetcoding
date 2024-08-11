class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        while matrix:
            result += matrix.pop(0)
            matrix = list(zip(*matrix))[::-1]
         # Append any remaining elements
        result += [element for row in matrix for element in row]
        return result

        