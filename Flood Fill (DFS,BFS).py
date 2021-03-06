'''
An image is represented by an m x n integer grid image where image[i][j] represents the pixel value of the image.

You are also given three integers sr, sc, and newColor. You should perform a flood fill on the image starting from the pixel image[sr][sc].

To perform a flood fill, consider the starting pixel, plus any pixels connected 4-directionally to the starting pixel of the same color as the starting pixel, plus any pixels connected 4-directionally to those pixels (also with the same color), and so on. Replace the color of all of the aforementioned pixels with newColor.

Return the modified image after performing the flood fill.

Example 1:
Input: image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, newColor = 2
Output: [[2,2,2],[2,2,0],[2,0,1]]
Explanation: From the center of the image with position (sr, sc) = (1, 1) (i.e., the red pixel), all pixels connected by a path of the same color as the starting pixel (i.e., the blue pixels) are colored with the new color.
Note the bottom corner is not colored 2, because it is not 4-directionally connected to the starting pixel.

Example 2:
Input: image = [[0,0,0],[0,0,0]], sr = 0, sc = 0, newColor = 2
Output: [[2,2,2],[2,2,2]]
'''

#Solution 1 - Depth First Search(DFS):
 #Time Complexity: O(N), where N is the number of pixels in the image. We might process every pixel.
 #Space Complexity: O(N), the size of the implicit call stack when calling dfs.

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
old=image[sr][sc]
m=len(image)
n=len(image[0])

def dfs(i,j):
  image[i][j]=newColor
  for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
    if 0<=x<m and 0<=y<n and image[x][y]==old:
      dfs(x,y)
      
if old != newColor:
  dfs(sr,sc)
print(image)

#Solution 2 - Breadth First Search

image = [[1,1,1],[1,1,0],[1,0,1]]
sr = 1
sc = 1
newColor = 2
oldcolor=image[sr][sc]
m=len(image)
n=len(image[0])
if oldcolor!=newColor:
  q=collections.deque([(sr,sc)])
  while q:
    i,j=q.popleft()
    image[i][j]=newColor
    for x,y in ((i-1,j),(i+1,j),(i,j-1),(i,j+1)):
      if 0<=x<m and 0<=y<n and image[x][y]==oldcolor:
        q.append((x,y))
print(image)
