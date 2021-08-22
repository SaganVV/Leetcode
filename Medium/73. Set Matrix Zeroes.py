class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_zeros = [[el==0 for el in row] for row in matrix]
        m = len(matrix)
        n = len(matrix[0])
        hor_zeros = [False for i in range(m)]
        vert_zeros = [False for i in range(n)]           
        for i in range(m):
            for j in range(n):
                if is_zeros[i][j]:
                    
                    if not hor_zeros[i]:
                        for z in range(n):
                            matrix[i][z] = 0
                    if not vert_zeros[j]:
                        for z in range(m):
                            matrix[z][j] = 0
