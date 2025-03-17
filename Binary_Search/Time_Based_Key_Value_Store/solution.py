# Solution 

class Solution:
    def __init__(self):
        self.keyStore = {}
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyStore:
            self.keyStore[key] = []
        self.keyStore[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = "" 
        values = self.keyStore.get(key, []) #why []?
        l = 0
        r = len(values) - 1 

        while l <= r:
            m = (l + r) // 2 
            if values[m][1] == timestamp:
                return values[m][0]
            elif values[m][1] < timestamp:
                l = m + 1 
                res = values[m][0]
            else: 
                r = m - 1 
        return res 

sol = Solution()  # creat only one Solution class
sol.set("lulu", "happy", 1)  
print(sol.get("lulu", 1))  # happy

sol.set("lulu", "sad", 3)  
print(sol.get("lulu", 4))  # sad