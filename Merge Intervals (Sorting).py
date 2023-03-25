'''
Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.


Example 1:

Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

Example 2:

Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

 

Constraints:

    1 <= intervals.length <= 104
    intervals[i].length == 2
    0 <= starti <= endi <= 104
'''

# Solution 1:

# Time Complexity : O(nlogn) + O(n) = O(nlogn)
# Space Complexity : O(n)

def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        res = []
        if len(intervals) == 0 or intervals == None:
            return []
        intervals.sort(key =lambda x: x[0])
        start = intervals[0][0]
        end = intervals[0][1]

        for i in intervals:
            if i[0] <= end:
                end = max(end, i[1])
            else:
                res.append([start,end])
                start = i[0]
                end = i[1]
        res.append([start,end])

        return res
