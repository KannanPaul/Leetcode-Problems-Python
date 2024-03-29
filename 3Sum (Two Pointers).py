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
# Time Complexity : O(nlogn)+ O(n*n) - where nlogn is sorting the list
# Space Complexity : O(M) where M is the number of solutions

def threeSum(self, nums: List[int]) -> List[List[int]]:
        ans = []
        n = len(nums)
        nums.sort()
       
        for i in range(n):
            if (i > 0 and nums[i] == nums[i-1]):
                continue
            low = i + 1
            high = n -1

            while low < high:
                sum = nums[i] + nums[low] + nums[high]
                if sum < 0:
                    low = low + 1
                elif sum > 0:
                    high = high - 1
                else:
                    ans = ans + [ [ nums[i] , nums[low] , nums[high] ] ]
                    low = low + 1
                    high = high -1

                    while (low < high and nums[low] == nums[low - 1]):
                        low = low + 1
                    while (low < high and nums[high] == nums[high + 1]):
                        high = high - 1
        return ans
       
# Solution 2 : Brute Force approach
# Time complexity : O(n*n*n)log(no.of triplets) 
# Space complexity : 2*O(no. of triplets)

def threeSum(self, nums: List[int]) -> List[List[int]]:
        setTriplet = set()
        ans = []
        n = len(nums)

        for i in range(n):
            for j in range(i+1, n):
                for k in range(j+1, n):
                    if nums[i]+ nums[j] + nums[k] == 0:
                        setTriplet.add(tuple(sorted([nums[i], nums[j], nums[k]])))
                    
        return setTriplet

       
  
# Solution 3 : Brute Force approach - optimized
# Time complexity : O(n*n)log(M) where M - adding values to set * M is varaible based on data
# Space complexity : O(n) + 2*O(no. of triplets) - where n - no. of data in tempset

def threeSum(self, nums: List[int]) -> List[List[int]]:
        setTriplet = set()
        ans = []
        n = len(nums)

        for i in range(n):
            tempset = set()
            for j in range(i+1, n):
                thirdnum = -(nums[i] + nums[j])
                if thirdnum in tempset:
                    setTriplet.add(tuple(sorted([nums[i], nums[j], thirdnum])))
                tempset.add(nums[j])
                    
        return setTriplet
