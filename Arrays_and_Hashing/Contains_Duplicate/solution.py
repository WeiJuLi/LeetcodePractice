#Solution

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        setNums = set(nums)
        return (len(nums) != len(setNums))
    
#Test cases

print(Solution().containsDuplicate([1,2,3,4])) #False
print(Solution().containsDuplicate([1,2,3,1])) #True



