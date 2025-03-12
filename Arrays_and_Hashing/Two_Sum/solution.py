# 1. create a dictionary to store all elements inside the input list. Key: char, Value: index.
# 2. for loop: store all of them
# 3. for loop: iterate through the whole list
#       find = target - nums[i]
#       if find in dictionary:
#         return [i, index of find]

# # Solution 1 
# from typing import List
# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         twoSumD = {}
#         for index, value in enumerate(nums):
#             twoSumD[value] = index 

#         for i, num in enumerate(nums):
#             find = target - nums[i]
#             if find in twoSumD and i != twoSumD[find]:
#                 return [i, twoSumD[find]]


# Solution 2 
from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        twoSum = {}
        #The purpose of twoSum is to store numbers that are waiting to be matched.

        for index, num in enumerate(nums):
            find = target - num
            if find in twoSum:
                return [twoSum[find], index]
            else: 
                #Put num into twoSum and wait for a match.
                twoSum[num] = index



#test
print(Solution().twoSum([2, 7, 11, 15], 9)) # [0, 1]
print(Solution().twoSum([3, 2, 4], 6)) # [1, 2]
print(Solution().twoSum([3, 3], 6)) # [0, 1]

# review
# Time Complexity: O(n), because I iterate the nums list once
# Space Complexity: O(n), because I use a dictionary to store the number I checked and its Index