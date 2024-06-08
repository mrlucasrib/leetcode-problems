from collections import deque
class Solution:
    def in_bounds(self, matrix, x, y):
        rows = len(matrix)
        cols = len(matrix[0])
        return 0 <= x < rows and 0 <= y < cols
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        row,col = len(mat), len(mat[0])
        queue = deque()
        for i in range(row):
            for j in range(col):
                if mat[i][j] == 0:
                    queue.append((i,j))
                else:
                    mat[i][j] = -1

        while queue:
            i,j = queue.popleft()   
            for x,y in (i+1,j), (i-1, j), (i, j+1), (i,j-1):
                if self.in_bounds(mat, x,y):
                    if mat[x][y] == -1:
                        mat[x][y] = mat[i][j] + 1
                        queue.append((x,y))
        return mat

        

