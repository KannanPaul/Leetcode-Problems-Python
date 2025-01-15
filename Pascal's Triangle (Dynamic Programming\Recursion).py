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
Time complexity : O(numRows^2) 
Space complexity : O(numRows)

def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]

        for i in range(1, numRows):
            res += [[res[i-1][0]]]
            for j in range(i-1):
                res[-1] += [ res[i-1][j] + res[i-1][j+1]]
            res[-1] += [res[i-1][-1]]
        
        return res

Solution 3: Recursion
Time complexity : O(numRows^2) 
Space complexity : O(numRows^2) space due to storing the entire triangle or previous rows in recursion.

 def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0:
            return []
        if numRows == 1:
            return [[1]]
        
        prevRows = self.generate(numRows - 1)
        newRow = [1] * numRows
        
        for i in range(1, numRows - 1):
            newRow[i] = prevRows[-1][i - 1] + prevRows[-1][i]
        
        prevRows.append(newRow)
        return prevRows
