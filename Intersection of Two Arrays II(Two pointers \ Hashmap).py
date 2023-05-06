'''
Intersection of Two Arrays II

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

# Solution 1 (Two Pointers):

# Time Complexity : If the lists are sorted, then the time complexity is O(N), Otherwise it is O(NlgN)
# Space Complexity : O(nums1) + O(nums2)

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        res = []
        n1 = len(nums1)
        n2 = len(nums2)
        i = 0
        j = 0

        while i < n1 and j < n2:
            if nums1[i] > nums2[j]:
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                res = res + [nums1[i]]
                i += 1
                j += 1
        return res
      
# Solution 2 (HashMap):

def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        n1dict = dict()
        for i in nums1:
            if i in n1dict:
                n1dict[i] += 1
            else:
                n1dict[i] = 1
        res=[]
        for j in nums2:
            if j in n1dict and n1dict[j]>0:
                res = res + [j]
                n1dict[j] -=1

        
        return res
