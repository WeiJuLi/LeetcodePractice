# 1. Create an empty dictionary `groups`
# 2. Loop through each word in the input list:
#    a. Create a list of size 26, filled with zeros
#    b. For each character in the word: - Convert the character to an index (e.g., 'a' = 0, 'b' = 1, ..., 'z' = 25) - Increase the count at that index
#    c. Convert the list into a tuple (to use as a dictionary key)
#    d. Add the word to `groups[key]`
# 3. Return all grouped anagrams as a list of lists

from typing import List
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for i in strs:
            freq = [0] * 26 
            for j in i:
                freq[ord(j) - ord('a')] += 1 
            groups[tuple(freq)].append(i)
        
        return list(groups.values())
    
#test
print(Solution().groupAnagrams([""])) 
print(Solution().groupAnagrams(["car", "rac"])) 
    
