#Solution

from typing import List
from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        sDict = defaultdict(int) 
        tDict = defaultdict(int)

        for i in range(len(s)):
            sDict[s[i]] += 1 
            tDict[t[i]] += 1 
        return sDict == tDict 
        
#test
print(Solution().isAnagram("anagram", "nagaram")) #True
print(Solution().isAnagram("rat", "car")) #False

#review
#Time Complexity: O(n) because I iterate through the strings once.
#Space Complexity: O(1) We have at most 26 different characters.

