#pseudocode

#Create a dictionary to store the numbers and their indices
#Iterate through the list of numbers
#Check if the number is already in the dictionary
#If it is, return True
#If it is not, add the number to the dictionary
#If no duplicates are found, return False

#Solution

from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums_map = {}
        for n in nums:
            if n in nums_map:
                return True
            nums_map[n] = n
        return False
    
#Test cases

print(Solution().containsDuplicate([1,2,3,4])) #False
print(Solution().containsDuplicate([1,2,3,1])) #True

#Review
#Time Complexity: O(n), because I iterate the nums list once
#Space Complexity: O(n), because I use a dictionary to store the number I checked and its Index

