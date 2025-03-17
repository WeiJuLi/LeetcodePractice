# 1. If len(piles) == h : return max(piles) 
# 2. We need to create two pointers. l = 1, r = max(piles) 
# 3. While loop : keep narrowing our searching range. While l <= r: O(logm)
#     4. a middle variable = (l + r) // 2 
#     5. Calculate hours required with speed = middle 
#     for loop: for each pile in piles: O(n)
#         hours += ceil(pile / middle)
#     6. Check if the total hours fit within h 
#     If hours <= h:
#         minK = middle # update minimum eating speed 
#         r = middle - 1 # Try smaller speeds
#     Else: 
#         l = middle + 1 # Increase speed to reduce total hours

# return minK



# Solution 
from typing import List
import math

class Solution:
    def koBana(self, piles: List[int], h: int) -> int:
        if len(piles) == h:
            return max(piles)
        l, r = 1, max(piles)
        minK = max(piles)

        while l <= r:
            middle = (l + r) // 2 
            hours = 0
            for pile in piles:
                hours += math.ceil(pile / middle)
            if hours <= h:
                minK = min(minK, middle)
                r = middle - 1 
            else:
                l = middle + 1 
        return minK

            
print(Solution().koBana([1,4,3,2], 9)) #2 

