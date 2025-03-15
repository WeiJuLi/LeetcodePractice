# Input: nums = [1, -1, 2, 0]
# Output: 4

# 0. if len(nums) == 0: return 0 

# 1. Convert the nums list into a set for fast lookups. set = {1, -1, 2, 0}
# 2. Initialize res = 0 to keep track of the longest sequence. res = 0 
# 3. Loop through each number in the set: 
#     Check if it's a starting number (i-1 is not in the set)
#     if it's a starting number:
#         set leng = 1, leng = 1 
#         While loop: Keep finding the following consecutive integer inside the set, untill we can't find it. (i + leng inside the set)
#             leng += 1, leng = 4
#         res = max(res, leng) 
#     else:
#         continue 
# 4. return res 


# Dry run: 
# 1. Happy case 
# 2. Edge case (add step 0)

# Solution 

from typing import List

class Solution:
    def longestCSeq(self, nums: List[int] ) -> int:
        if len(nums) == 0: 
            return 0 
        
        numSet = set(nums)
        res = 0 

        for num in numSet:
            if (num - 1) in numSet:
                continue
            else:
                leng = 1 
                while (num + leng) in numSet:
                    leng += 1 
                res = max(res, leng)
        
        return res 
    
print(Solution().longestCSeq([1, -1, 2, 0])) #4 
    
    
                

        
