# Solution 
from typing import List

class Solution:
    def biSearch(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 

        while l <= r:
            middle = (l + r) // 2 
            if target == nums[middle]:
                return middle 
            elif target < nums[middle]:
                r = middle - 1 
            else: 
                l = middle + 1 
        return -1 
    

print(Solution().biSearch([1, 2, 3, 4], 4)) #3
print(Solution().biSearch([1, 2, 3, 5], 4)) #-1