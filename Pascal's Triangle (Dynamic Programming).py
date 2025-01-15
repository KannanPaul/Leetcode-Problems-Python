'''
Given an integer numRows, return the first numRows of Pascal's triangle.

In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:

 

Example 1:

Input: numRows = 5
Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]

Example 2:

Input: numRows = 1
Output: [[1]]

 

Constraints:

    1 <= numRows <= 30
'''
# Time Complexity : O(n*n) where n = no. of rows
# Space Complexity : O(n*n) where n = no. of rows

# Solution 1 : 

def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(1,numRows):
            temp = []
            for i in range(len(res[-1])-1):
                temp = temp + [res[-1][i] + res[-1][i+1]]
            temp = [1] + temp + [1]
            res = res + [temp]
        
        return res


Solution 2:

def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            res += [[res[i-1][0]]]
            for j in range(i-1):
                res[-1] += [ res[i-1][j] + res[i-1][j+1]]
            res[-1] += [res[i-1][-1]]
        
        return res
