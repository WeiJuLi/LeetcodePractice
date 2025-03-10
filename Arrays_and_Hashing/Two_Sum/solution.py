# pseudocode

# Initialize:
#   Create empty dictionary nums_map to store {number: index}

# Process:
#   FOR each index, num in nums:
#       Calculate diff = target - num
#       IF diff exists in nums_map:
#           RETURN [nums_map[diff], current_index]
#       ELSE:
#           Add num:index to nums_map
#   
#   IF no solution found:
#       RETURN empty list

# Solution
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_map = {}
        for index, num in enumerate(nums):
            diff = target - num
            if diff in nums_map:
                return [nums_map[diff], index]
            else:
                nums_map[num] = index
        return []

#test
print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(Solution().twoSum([3, 2, 4], 6)) # [1, 2]
print(Solution().twoSum([3, 3], 6)) # [0, 1]

# review
# Time Complexity: O(n), because I iterate the nums list once
# Space Complexity: O(n), because I use a dictionary to store the number I checked and its Index