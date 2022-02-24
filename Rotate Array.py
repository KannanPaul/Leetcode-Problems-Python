

#Solution:

k = k % len(nums)
nums[:] = nums[-k:] + nums[:-k]
