# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:
        dummy = TreeNode(0)
        current = dummy

        def inorder(node):
            nonlocal current

            if not node:
                return

            inorder(node.left)

            node.left = None
            current.right = node
            current = node

            inorder(node.right)

        inorder(root)
        return dummy.right