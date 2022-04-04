'''
You are given an m x n grid where each cell can have one of three values:

0 representing an empty cell,
1 representing a fresh orange, or
2 representing a rotten orange.
Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.

Example 1:
Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
Output: 4

Example 2:
Input: grid = [[2,1,1],[0,1,1],[1,0,1]]
Output: -1
Explanation: The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.

Example 3:
Input: grid = [[0,2]]
Output: 0
Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.
'''

#Solution 1 - (Breadth First search)
# Time complexity: O(rows * cols) -> each cell is visited at least once
# Space complexity: O(rows * cols) -> in the worst case if all the oranges are rotten they will be added to the queue

def orangesRotting(self, grid: List[List[int]]) -> int:
        import collections
        m=len(grid)  
        n=len(grid[0])
        rotten=collections.deque()
        fresh=0
        for i in range(m):
            for j in range(n):
                if grid[i][j]==2:
                    rotten.append((i,j))
                if grid[i][j]==1:
                    fresh+=1
        minute_passed=0
        
        while rotten and fresh>0:
            minute_passed +=1
            for _ in range(len(rotten)):
                x,y=rotten.popleft()            
                for r,c in ((x+1,y),(x-1,y),(x,y+1),(x,y-1)):
                    if 0<=r<m and 0<=c<n and grid[r][c]==1:
                        fresh-=1
                        grid[r][c]=2
                        rotten.append((r,c))
        
        return minute_passed if fresh==0 else -1
