'''
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.

Example 1:

Input: nums = [3,2,3]
Output: 3

Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

'''


# Solution 1 :
# Time Complexity : O(N)
# Space Complexity : O(1)

def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = 0
        
        for num in nums:
            if count == 0:
                candidate = num
            if num == candidate:
                count += 1
            else:
                count -= 1
        
        return candidate

     
# Solution 2 :
# Time Complexity : O(N)
# Space Complexity : O(N)

def majorityElement(self, nums: List[int]) -> int:
        hash = dict()
        max = 0
        value = None
        for num in nums:
            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1
            if hash[num] > max:
                max = hash[num]
                value = num
        return value
