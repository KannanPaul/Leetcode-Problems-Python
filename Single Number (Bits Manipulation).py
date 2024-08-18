'''
Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.
You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:
Input: nums = [2,2,1]
Output: 1

Example 2:
Input: nums = [4,1,2,1,2]
Output: 4

Example 3:
Input: nums = [1]
Output: 1
'''

#Solution 1 : Bits Manipulation 
# Time complexity - O(n)
# Space complexity - O(1)

Optimal Approach(Using XOR): 

Two important properties of XOR are the following:

XOR of two same numbers is always 0 i.e. a ^ a = 0. ←Property 1.
XOR of a number with 0 will result in the number itself i.e. 0 ^ a = a.  ←Property 2

So, if we perform the XOR of all the numbers of the array elements, we will be left with a single number.

def singleNumber(self, nums: List[int]) -> int:
        singlenum=0
        for i in nums:
            singlenum^=i
        return singlenum
