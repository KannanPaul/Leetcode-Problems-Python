'''
Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

 

Example 1:

Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]
Explanation: 
nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
The distinct triplets are [-1,0,1] and [-1,-1,2].
Notice that the order of the output and the order of the triplets does not matter.

Example 2:

Input: nums = [0,1,1]
Output: []
Explanation: The only possible triplet does not sum up to 0.

Example 3:

Input: nums = [0,0,0]
Output: [[0,0,0]]
Explanation: The only possible triplet sums up to 0.

 

Constraints:

    3 <= nums.length <= 3000
    -105 <= nums[i] <= 105

'''

# Solution 1:
# Time Complexity : O( N*N)
# Space Complexity : O(M) where M is the number of solutions

def threeSum(self, nums: List[int]) -> List[List[int]]:
        res=[]
        nums.sort()

        for i in range(len(nums)-2):
            if i==0 or (i>0 and nums[i] != nums[i-1]):
                low = i + 1
                high = len(nums)-1
                sum = 0 - nums[i]
            while low < high:
                if nums[low] + nums[high] == sum:
                    res.append([nums[i], nums[low], nums[high]])
                    while low < high and nums[low] == nums[low + 1]:
                            low += 1
                    while low < high and nums[high] == nums[high - 1]:
                            high -= 1
                    low += 1
                    high -= 1
                elif nums[low]+ nums[high] < sum:
                    low += 1
                elif nums[low]+ nums[high] > sum:
                    high -= 1
        return res
