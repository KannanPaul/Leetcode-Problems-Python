'''
Given an integer array nums, find the
subarray
with the largest sum, and return its sum.

 

Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:

Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.

 

Constraints:

    1 <= nums.length <= 105
    -104 <= nums[i] <= 104

 

Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.

'''

# Solution 1: (Kadane's Algorithm)
# Time Complexity : O(N), for iterating over nums once
# Space Complexity : O(1), only constant extra space is being used.

def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_sum = nums[0]
        cur_max = 0
        n = len(nums)

        for index in range(n):
            cur_max = max(cur_max + nums[index], nums[index])
            if max_sum < cur_max:
                max_sum = cur_max
            
        return max_sum

# Solution 2: (Kadane's Algorithm)
 def maxSubArray(self, nums: List[int]) -> int:
        max_so_far = -sys.maxsize-1
        max_ending_here = 0
        size=len(nums)    
        for i in range(0, size): 
            max_ending_here = max_ending_here + nums[i] 
            if (max_so_far < max_ending_here): 
                max_so_far = max_ending_here 
  
            if max_ending_here < 0: 
                max_ending_here = 0   
        return max_so_far

# Solution 3: (Divide & Conquer)
# Time Complexity : O(NlogN), the recurrence relation can be written as T(N) = 2T(N/2) + O(N) since we are recurring for left and right half (2T(N/2)) and also calculating maximal subarray including mid element which takes O(N) to calculate. Solving this recurrence using master theorem, we can get the time complexity as O(NlogN)
# Space Complexity : O(logN), required by recursive stack

def maxSubArray(self, nums):
        def maxSubArray(A, L, R):
            if L > R: return -inf
            mid, left_sum, right_sum, cur_sum = (L + R) // 2, 0, 0, 0
            for i in range(mid-1, L-1, -1):
                left_sum = max(left_sum, cur_sum := cur_sum + A[i])
            cur_sum = 0
            for i in range(mid+1, R+1):
                right_sum = max(right_sum, cur_sum := cur_sum + A[i])
            return max(maxSubArray(A, L, mid-1), maxSubArray(A, mid+1, R), left_sum + A[mid] + right_sum)
        return maxSubArray(nums, 0, len(nums)-1)


# For the same question to Print Maximum Subarray
Solution:

import sys

def maxSubarraySum(arr, n):
    maxi = -sys.maxsize - 1  # maximum sum
    sum = 0

    start = 0
    ansStart, ansEnd = -1, -1
    for i in range(n):

        if sum == 0:
            start = i  # starting index

        sum += arr[i]

        if sum > maxi:
            maxi = sum

            ansStart = start
            ansEnd = i

        # If sum < 0: discard the sum calculated
        if sum < 0:
            sum = 0

    # printing the subarray:
    print("The subarray is: [", end="")
    for i in range(ansStart, ansEnd + 1):
        print(arr[i], end=" ")
    print("]")

    # To consider the sum of the empty subarray
    # uncomment the following check:

    # if maxi < 0:
    #     maxi = 0

    return maxi

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
n = len(arr)
maxSum = maxSubarraySum(arr, n)
print("The maximum subarray sum is:", maxSum)


