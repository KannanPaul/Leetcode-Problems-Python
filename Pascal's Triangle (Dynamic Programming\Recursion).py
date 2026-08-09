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

Question 2:
To print the Nth row of the pascal triangle we can take advantage of the relationship between Nth element and binomial coefficients.
In a pascal's triangle, the Nth row contains the binomial coefficients C(N-1, 0), C(N-1, 1) and so on till C(N-1, N-1). Thus we can simply calculate all these values to return the Nth row of pascal triangle.
Instead of computing full factorials, we can start with the first value as 1, and use the relation C(n, k) = C(n, k−1) × (n−k+1) / k to compute the next value from the previous one in constant time.

Complexity Analysis
Time Complexity: O(N), we iterate N times to compute each element of the row in O(1) time using the direct relation.
Space Complexity: O(N), additional space used for storing the Nth row. 




Question 3:
To find the element at the coordinates (R,C) where R is the row number and C is the Column number, we can simply simulate the generation of pascal's triangle for R rows. In Pascal’s Triangle, the element at row R and column C corresponds to the binomial coefficient (r-1)C(c-1). To calculate this binomial coefficient, we can simply apply the formula of binomial coefficient i.e. (r-1)!/(c-1)!(r-c)!.
Instead of computing full factorials (which can overflow and be slow), we can multiply and divide in a loop to compute the coefficient efficiently.

Complexity Analysis
Time Complexity: O(min(c,r−c)), The loop runs for min(c−1,r−c) iterations because binomial coefficients are symmetric.
Space Complexity: O(1), constant additional space is used. 

# Solution class to find the (r, c) element of Pascal's Triangle
class Solution:
    # Function to compute binomial coefficient (nCr)
    def findPascalElement(self, r, c):
        # Element is C(r-1, c-1)
        n = r - 1
        k = c - 1

        result = 1

        # Compute C(n, k) using iterative formula
        for i in range(k):
            result *= (n - i)
            result //= (i + 1)

        return result


# Main code to test the solution
if __name__ == "__main__":
    sol = Solution()
    r, c = 5, 3
    print(sol.findPascalElement(r, c))
