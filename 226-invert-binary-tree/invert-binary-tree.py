# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.help(root)
        return root

    def help(self, root):
        if not root:
            return None
        else:
            temp = root.left
            root.left = root.right
            root.right = temp
            self.help(root.left)
            self.help(root.right)

        