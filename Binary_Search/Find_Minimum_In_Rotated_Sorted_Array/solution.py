# 0. If len(nums) == 1: return nums[0] is the smallest 
# 1. Initialize l, r pointers. l = 0, r = len(nums) - 1 
# 2. While loop: l < r (最後再判斷，是l <= r還是l < r) O(logn)
#     middle = (l + r) // 2 
#     if nums[middle] < nums[r], the minimum must be in the left half, so set r = middle
#     Otherwise, the minimum must be in the right half, so let l = middle + 1 
# 3. While l == r, return nums[l]

# nums = [3, 4, 1, 2]

# Solution 
from typing import List

class Solution:
    def minBinary(self, nums: List[int]) -> int:
        if len(nums) == 1 :
            return nums[0]
        l, r = 0 , len(nums) - 1
        while l < r:
            m = (l + r) // 2 
            if nums[m] < nums[r]:
                r = m #nums[m - 1] might out of bound
            else: #nums[m] >= nums[r]
                l = m + 1 #nums[m] must bigger than nums[m + 1]
        return nums[l]
    

print(Solution().minBinary([1])) #1
print(Solution().minBinary([3,4,1,2])) #1

