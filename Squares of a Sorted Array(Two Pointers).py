'''
Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].

Example 2:
Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]
'''
#Solution -1 :(Two Pointers - O(n) time complexity and O(n) auxillary space)

answer = [0] * len(nums)
l, r = 0, len(nums) - 1
while l <= r:
  left, right = abs(nums[l]), abs(nums[r])
  if left > right:
    answer[r - l] = left * left
    l += 1
  else:
    answer[r - l] = right * right
    r -= 1
  
print(answer)


#solution 2: (Two Pointers - O(n) time complexity and O(n) auxillary space)

def sortedSquares(self, nums: List[int]) -> List[int]:
        l=0
        h=len(nums)-1
        r=[0]*len(nums)
        n=h
        while l<=h:
            ls= nums[l]**2
            hs= nums[h]**2
            if ls <=hs:
                r[n]=hs
                h=h-1
            elif ls >= hs:
                r[n]=ls
                l=l+1
            n=n-1
        return r 
