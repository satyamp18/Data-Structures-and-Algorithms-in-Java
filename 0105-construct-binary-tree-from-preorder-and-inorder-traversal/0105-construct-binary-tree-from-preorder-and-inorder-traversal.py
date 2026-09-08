# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder, inorder):
        pos = {val: i for i, val in enumerate(inorder)}
        pre_index = 0

        def build(left, right):
            nonlocal pre_index

            if left > right:
                return None

            root_val = preorder[pre_index]
            pre_index += 1

            root = TreeNode(root_val)

            mid = pos[root_val]

            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)

            return root

        return build(0, len(inorder) - 1)