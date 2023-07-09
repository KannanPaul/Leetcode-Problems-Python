'''
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.

 

Example 1:

Input: points = [[1,1],[2,2],[3,3]]
Output: 3

Example 2:

Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4

 

Constraints:

    1 <= points.length <= 300
    points[i].length == 2
    -104 <= xi, yi <= 104
    All the points are unique.

'''

# Solution 1: (Math Geomtry using hash table)
# Time complexity: O(N^2)
# Space complexity: O(N) as we track only N-1 lines in total

def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n <= 2:
            return n
        
        def find_slope(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            if x2 - x1 == 0:
                return inf
            return (y2 - y1) / (x2 - x1)

        res = 1
        for i in range(n):
            slopes = {}
            for j in range(i+1,n):
                temp = find_slope(points[i], points[j])
                if temp in slopes:
                    slopes[temp] += 1
                else:
                    slopes[temp] = 1
                res = max(slopes[temp], res)
        return res+1
