# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def helper(self, node, mp):
        if not node:
            return 0

        leftSum = self.helper(node.left, mp)
        rightSum = self.helper(node.right, mp)

        maxValue = max(leftSum + rightSum + node.val, node.val + leftSum, node.val + rightSum, node.val)
        mp["maxValue"] = max(maxValue, mp["maxValue"])
        pathValue = max(leftSum + node.val, rightSum + node.val, node.val)
        return pathValue

    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        mp = {"maxValue": -2 ^ 31}
        self.helper(root, mp)
        return mp["maxValue"]


if __name__ == '__main__':
    root = TreeNode(1)
    firstNode = TreeNode(2)
    root.left = firstNode
    solution = Solution()
    res = solution.maxPathSum(root)
    print res
