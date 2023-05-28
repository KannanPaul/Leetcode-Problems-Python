'''
You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:

Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]

 

Constraints:

    n == matrix.length == matrix[i].length
    1 <= n <= 20
    -1000 <= matrix[i][j] <= 1000
'''

# Solution 1 : Reverse on Diagonal and then Reverse Left to Right

# Complexity Analysis
'''
Let (M) be the number of cells in the grid.

    Time complexity : O(n*n) + O(n*n)

    Space complexity : O(1)
'''

def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        self.transpose(matrix)
        self.reflect(matrix)

    def transpose(self, matrix):
        row = len(matrix)
        for i in range(row):
            for j in range(i+1, row):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def reflect(self, matrix):
        row = len(matrix)
        for i in range(row):
            for j in range(row//2):
                matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]

# Solution 2 : Changing rows postion & transpose the matrix

def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        l = 0
        r = len(matrix) - 1

        while l <= r:
            matrix[l], matrix[r] = matrix[r], matrix[l]
            l += 1 
            r -= 1

        
        for i in range(len(matrix)):
            for j in range(i,len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        
# Other Problems
# Rotate 180 degree


# matrix = [[1,2,3],[4,5,6],[7,8,9]]
 
for i in range(len(matrix)):
    for j in range(len(matrix[0])//2):
        matrix[i][j], matrix[i][-j-1] = matrix[i][-j-1], matrix[i][j]
         
l = 0
r = len(matrix) - 1

while l<=r:
    matrix[l],matrix[r] = matrix[r],matrix[l]
    l += 1
    r -= 1

matrix = [[9, 8, 7], [6, 5, 4], [3, 2, 1]]
