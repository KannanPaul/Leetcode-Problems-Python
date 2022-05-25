'''
Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]
'''
#Solution 1 : O(n)-time complexity, O(1)-space complexity
slow=0
n=len(nums)
for fast in range(n):
  if nums[fast] !=0 and nums[slow]==0:
    nums[fast], nums[slow]= nums[slow],nums[fast]
              
  if nums[slow]!=0:
    slow+=1

print(nums)

solution 2: O(n)-time complexity, O(1)-space complexity
    def moveZeroes(self, nums: List[int]) -> None:
        i=0
        j=0
        n=len(nums)
        
        while i<n and j<n:
            if nums[j]!=0:
                nums[j],nums[i]=nums[i],nums[j]
                i+=1
            j+=1
            
        return nums
      
solution 3:
  def moveZeroes(self, nums: List[int]) -> None:
        n=len(nums)
        last_zero=0
        for i in range(n):
            if nums[i] !=0:
                nums[i],nums[last_zero]=nums[last_zero],nums[i]
                last_zero+=1
        return nums
        
