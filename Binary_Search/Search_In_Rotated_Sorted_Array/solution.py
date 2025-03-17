#  1. create two pointers. l = 0, r = len(nums) - 1 
#  2. While loop: keep narrowing the search range untill l > r 
#     middle = (l + r) // 2 
#     if target == nums[m] return m

#     3. Find the sorted sequence to do binary search

#     4. nums[m] <= nums[r] : the right side of nums[m] is sorted

#         if target is not betweeb nums[m] and nums[n] : the target might at the left half r = m - 1 
#         else: l = m + 1 

#     5. nums[m] > nums[r] : the left side of nums[m] is sorted 

#         if target is not between nums[l] and nums[m] : the target might at the right half. l = m + 1 
#         else: r = m - 1 

# 3. while l > r and can't find the target 
# return - 1 


# Solution 
from typing import List

class Solution:
    def searchRotate(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1 
        while l <= r:
            m = (l + r) // 2 

            if nums[m] == target:
                return m

            if nums[m] <= nums[r]: #right half is sorted 
                if nums[m] < target <= nums[r]:
                    l = m + 1 
                else:
                    r = m - 1 
            
            else : #left half is sorted 
                if nums[l] <= target < nums[m]:
                    r = m - 1 
                else: 
                    l = m + 1 
        return -1 
    

print(Solution().searchRotate([0], 1)) #-1
print(Solution().searchRotate([6,1,3,5], 3)) #2