'''
You are given an m x n integer matrix matrix with the following two properties:

    Each row is sorted in non-decreasing order.
    The first integer of each row is greater than the last integer of the previous row.

Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

 

Example 1:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:

Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

 

Constraints:

    m == matrix.length
    n == matrix[i].length
    1 <= m, n <= 100
    -104 <= matrix[i][j], target <= 104

'''

# Solution 1 :

# Time Complexity : O(log m*n) where m - no. of rows & n - no. of columns
# Space Complexity : O(1) 

def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        row = len(matrix)
        col = len(matrix[0])
        low = 0
        high = row*col -1
        
        while low <= high:
            mid = (low + high)//2
            value = matrix[mid//col][mid%col]
            if target == value:
                return True
            elif target > value:
                low = mid + 1
            elif target < value: 
                high = mid - 1

        return False
