class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        
        m =  len(matrix)
        n = len(matrix[0])

        for i in range(0,m):
                for j in range(0,n):
                        if i < j:
                                matrix[i][j],matrix[j][i] = matrix[j][i],matrix[i][j]
        # print(matrix)
        for i in range(0,m):
                for j in range(0,n//2):
                        matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]