'''
Given two integer arrays nums1 and nums2, return an array of their intersection. Each element in the result must appear as many times as it shows in both arrays and you may return the result in any order.

 

Example 1:

Input: nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

Example 2:

Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
Output: [4,9]
Explanation: [9,4] is also accepted.

 

Constraints:

    1 <= nums1.length, nums2.length <= 1000
    0 <= nums1[i], nums2[i] <= 1000

'''

# Solution 1:

# TIME COMPLEXITY : O(NlogN)
# SPACE COMPLEXITY : O(1) 

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        i = 0
        j = 0
        res = []
        nums1.sort()
        nums2.sort()
        n1 = len(nums1)
        n2 = len(nums2)
        while i < n1 and j < n2:
            if nums1[i] < nums2[j]:
                i+=1
            elif nums1[i] > nums2[j]:
                j+=1
            else:
                res.append(nums1[i])
                i+=1
                j+=1
        return res
