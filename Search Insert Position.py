'''
Given a sorted array of distinct integers and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.
You must write an algorithm with O(log n) runtime complexity.

Example 1:
Input: nums = [1,3,5,6], target = 5
Output: 2

Example 2:
Input: nums = [1,3,5,6], target = 2
Output: 1

Example 3:
Input: nums = [1,3,5,6], target = 7
Output: 4
'''

#Solution -1:

def search(nums,target,low,high):
  while low <= high:
    mid=(low+high)//2
    if target==nums[mid]:
        return mid
    elif nums[mid] <target:
        low=mid+1
    else:
        high=mid-1
  return low

nums = [1,3,5,6]
target = 2
low=0
high=len(nums)-1
print(search(nums,target,low,high))


#Solution -2:
 def search(nums,target,low,high):
    if not nums:
        return 0
    for i, num in enumerate(nums):
        if num >= target:
            return i
    return len(nums)
    
nums = [1,3,5,6]
target = 2
low=0
high=len(nums)-1

print(search(nums,target,low,high))
