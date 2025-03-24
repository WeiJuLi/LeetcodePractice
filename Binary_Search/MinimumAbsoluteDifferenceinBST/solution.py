from typing import Optional

class TreeNode(object):
     def __init__(self, val=0, left=None, right=None):
         self.val = val
         self.left = left
         self.right = right

# Iteration 
class Solution(object):
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
            cur, stack, minDiff, prev = root, [], 10**5, -10**5
            
            while stack or cur:
                while cur:
                    stack.append(cur)
                    cur = cur.left
                node = stack.pop()
                minDiff = min(minDiff, node.val - prev)
                prev = node.val
                cur = node.right
            
            return minDiff


# Recusion 
# self. 的意思是：這個變數是屬於這個 class（物件）本身的。
# 如果你在遞迴函式 inorder() 裡面要用到外面的變數（像 prev 和 minDiff），你必須加上 self.，這樣才能跨函式存取與修改。
# 否則 Python 會當作這是函式內部的區域變數（local variable），就沒辦法保存值或傳遞給下一層。

class Solution:
    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        self.prev = None
        self.minDiff = float('inf')

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            
            if self.prev is not None:
                self.minDiff = min(self.minDiff, node.val - self.prev)
            self.prev = node.val
            
            inorder(node.right)

        inorder(root)
        return self.minDiff