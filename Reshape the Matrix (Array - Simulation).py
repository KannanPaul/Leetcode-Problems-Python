'''
In MATLAB, there is a handy function called reshape which can reshape an m x n matrix into a new one with a different size r x c keeping its original data.

You are given an m x n matrix mat and two integers r and c representing the number of rows and the number of columns of the wanted reshaped matrix.

The reshaped matrix should be filled with all the elements of the original matrix in the same row-traversing order as they were.

If the reshape operation with given parameters is possible and legal, output the new reshaped matrix; Otherwise, output the original matrix.

 

Example 1:

Input: mat = [[1,2],[3,4]], r = 1, c = 4
Output: [[1,2,3,4]]

Example 2:

Input: mat = [[1,2],[3,4]], r = 2, c = 4
Output: [[1,2],[3,4]]

 

Constraints:

    m == mat.length
    n == mat[i].length
    1 <= m, n <= 100
    -1000 <= mat[i][j] <= 1000
    1 <= r, c <= 300

'''

# Solution 1 :
# Time Complexity : O(n*m) where n = no. of rows & m = no. of columns
# Space Complexity : O(n*m) where n = no. of rows & m = no. of columns

def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        flat = []
        newMat = []
        for row in mat:
            for num in row:
                flat.append(num)
                
        if r * c != len(flat):   # when given parameters is NOT possible and legal
            return mat
        else:
            for index in range(r):
                newMat.append(flat[index * c : index * c + c])
            return newMat

           
# Solution 2 :
 def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])
        result = [[]]
        if r * c != m*n:
            return mat

        for i in range(m):
            for j in range(n):
                if len(result[-1]) < c:
                    result[-1] = result[-1]+[mat[i][j]]
                else:
                    result= result +[[mat[i][j]]]
        
        return result
       
       
 # Solution 3 :
 
 def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        temp = []
        for row in mat:
            for col in row:
                temp = temp + [col]
        
        if len(temp) != r*c:
            return mat
         
        res=[[]]
        for value in temp:
            if len(res[-1]) < c:
                res[-1] = res[-1] + [value]
            else:
                res =  res + [[value]]
        return res
       
 # Solution 4 :
 
 def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        values=[]
        res=[]
        if r*c != len(mat)*len(mat[0]):
            return  mat
        for row in mat:
            for col in row:
                values.append(col)
        index = 0
        cc = c
        while index < len(values):
            temp = []
            while cc > 0:
                t.append(values[index])
                cc -= 1
                index += 1
            res.append(t)
            cc = c
        return res
       
       
 
