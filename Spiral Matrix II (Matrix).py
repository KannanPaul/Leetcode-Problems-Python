'''
Spiral Matrix II
Medium
5.7K
234
Companies

Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.

 

Example 1:

Input: n = 3
Output: [[1,2,3],[8,9,4],[7,6,5]]

Example 2:

Input: n = 1
Output: [[1]]

 

Constraints:

    1 <= n <= 20
'''

# Solution 1 : Traverse Layer by Layer in Spiral Form

# Time Complexity: O(n2)\mathcal{O}(n^2)O(n2). Here, nnn is given input and we are iterating over n⋅nn\cdot nn⋅n matrix in spiral form.
# Space Complexity: O(1)\mathcal{O}(1)O(1) We use constant extra space for storing cntcntcnt.

def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        cnt = 0

        matrix = [ [0]*n for i in range(n)]

        while left <= right and top <= bottom:
            for j in range(left, right+1):
                cnt = cnt + 1
                matrix[top][j] = cnt
    
            top = top + 1

            for i in range(top,bottom+1):
                cnt = cnt + 1
                matrix[i][right] = cnt

            right = right - 1

            for j in range(right,left-1, -1):
                cnt = cnt + 1
                matrix[bottom][j] = cnt

            bottom = bottom - 1

            for i in range(bottom, top-1, -1):
                cnt = cnt + 1
                matrix[i][left] = cnt
            
            left = left + 1

        return matrix


# Solution 2:

# Time Complexity: O(n2)\mathcal{O}(n^2)O(n2). Here, nnn is given input and we are iterating over n⋅nn\cdot nn⋅n matrix in spiral form.
# Space Complexity: O(1)\mathcal{O}(1)O(1) We use constant extra space for storing cntcntcnt.

def generateMatrix(self, n: int) -> List[List[int]]:
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        cnt = 0

        matrix = [ [0]*n for i in range(n)]

        while left <= right and top <= bottom:
            for j in range(left, right+1):
                cnt = cnt + 1
                matrix[top][j] = cnt
    
            top = top + 1

            for i in range(top,bottom+1):
                cnt = cnt + 1
                matrix[i][right] = cnt

            right = right - 1

            if top <= bottom:
                for j in range(right,left-1, -1):
                    cnt = cnt + 1
                    matrix[bottom][j] = cnt
                bottom = bottom - 1

            if left < right:
                for i in range(bottom, top-1, -1):
                    cnt = cnt + 1
                    matrix[i][left] = cnt
                left = left + 1

        return matrix

# Solurion 3: Optimized spiral traversal

# Time Complexity: O(n2)\mathcal{O}(n^2)O(n2). Here, nnn is given input and we are iterating over n⋅nn\cdot nn⋅n matrix in spiral form.
# Space Complexity: O(1)\mathcal{O}(1)O(1) We use constant extra space for storing cntcntcnt.

def generateMatrix(self, n: int) -> List[List[int]]:
        result = [[0] * n for _ in range(n)]
        cnt = 1;
        dir= [[0, 1], [1, 0], [0, -1], [-1, 0]]
        d = 0;
        row = 0;
        col = 0;
        while cnt <= n * n:
            result[row][col] = cnt
            cnt = cnt + 1
            r = (row + dir[d][0]) % n
            c = (col + dir[d][1]) % n

            ## change direction if next cell is non zero
            if result[r][c] != 0:
                d = (d + 1) % 4

            row += dir[d][0];
            col += dir[d][1];
        
        return result;
