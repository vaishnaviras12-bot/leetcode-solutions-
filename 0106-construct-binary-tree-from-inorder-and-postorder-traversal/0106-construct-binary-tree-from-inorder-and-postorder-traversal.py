# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        if not inorder:
            return None

        root = postorder.pop()
        a = inorder.index(root)
        bt = TreeNode(root)
        bt.right = self.buildTree(inorder[a + 1:], postorder)
        bt.left = self.buildTree(inorder[:a], postorder)

        return bt
        