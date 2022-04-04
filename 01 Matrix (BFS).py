'''
Given an m x n binary matrix mat, return the distance of the nearest 0 for each cell.
The distance between two adjacent cells is 1.

Example 1:
Input: mat = [[0,0,0],[0,1,0],[0,0,0]]
Output: [[0,0,0],[0,1,0],[0,0,0]]

Example 2:
Input: mat = [[0,0,0],[0,1,0],[1,1,1]]
Output: [[0,0,0],[0,1,0],[1,2,1]]
'''

#Solution 1 - (Depth First Search)
Complexity Analysis
Time complexity: O(r \cdot c)O(r⋅c)
Since, the new cells are added to the queue only if their current distance is greater than the calculated distance, cells are not likely to be added multiple times.
Space complexity: O(r \cdot c)O(r⋅c)
An additional O(r \cdot c)O(r⋅c) space is required to maintain the queue.

def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
     import collections
     q=collections.deque()
     m=len(mat)
     n=len(mat[0])
        
    for i in range(m):
      for j in range(n):
        if mat[i][j]==0:
          q.append((i,j))
        else:
          mat[i][j]=-1
            
    while q:
      x,y=q.popleft()
      for r,c in [(1,0),(-1,0),(0,1),(0,-1)]:
        newx,newy=x+r, y+c
        if 0<=newx<m and 0<=newy<n and mat[newx][newy]==-1:
           mat[newx][newy]=mat[x][y]+1
           q.append((newx,newy))
                    
     return mat
