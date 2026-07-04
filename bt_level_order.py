#102.Binary Tree Level Order Traversal
#Time Complexity: O(n)
#Space Complexity: O(n)
from collections import deque
from typing import Optional
from typing import List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        queue=deque([root])
        ans=[]
        while queue:
            current_level=[]
            for _ in range(len(queue)):
                node=queue.popleft()
                current_level.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            ans.append(current_level)
        return ans
        