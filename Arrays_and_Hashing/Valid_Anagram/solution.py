#pseudocode

#Create a dictionary to store the characters and their frequencies for both strings s and t
#Iterate through the strings and store the characters and their frequencies in the dictionary
#Compare the two dictionaries
#If they are identical, return True
#Otherwise, return False    

#Solution

from typing import List

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_map = {}
        t_map = {}
        
        for char in s:
            if char in s_map:
                s_map[char] += 1
            else:
                s_map[char] = 1
        
        for char in t:
            if char in t_map:
                t_map[char] += 1
            else:
                t_map[char] = 1
                
        return s_map == t_map
        
#test
print(Solution().isAnagram("anagram", "nagaram")) #True
print(Solution().isAnagram("rat", "car")) #False

#review
#Time Complexity: O(n), because I iterate through the strings once
#Space Complexity: O(n), because I use two dictionaries to store the characters and their frequencies
