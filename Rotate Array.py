'''
Given an array, rotate the array to the right by k steps, where k is non-negative.

Example 1:
Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]

Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]

Example 2:
Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]

Explanation: 
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
'''

#Solution 1:  

k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]

#Solution 2:  O(n)-time complexity ,O(1)-space complexity

def reverse(nums,i,j):
            while i <=j:
                nums[i],nums[j]=nums[j],nums[i]
                i+=1
                j-=1
        
        if k > len(nums):
            k %= len(nums)
            
        if k>0:
            reverse(nums,0, len(nums)-1)
            reverse(nums,0,k-1)
            reverse(nums,k,len(nums)-1)
        
        return nums
