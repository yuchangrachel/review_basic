# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    """
    Question: Invert BT layer by layer
    1. Swap cur node to other side instead of create new tree
    2. T O(n), S O(h), if balance tree will be O(logn)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        # l means left subtree of root
        l = root.left
        # r means right subtree of root
        r = root.right
        # let root.left pointing to r
        # let root.right pointing to l
        root.left = self.invertTree(r)
        root.right = self.invertTree(l)
        return root
