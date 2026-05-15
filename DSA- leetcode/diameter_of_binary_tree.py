# Definition of Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


class Solution:
    def diameterOfBinaryTree(self, root):
        self.diameter = 0

        def height(node):
            if node is None:
                return 0

            left = height(node.left)
            right = height(node.right)

            # update diameter (number of edges)
            self.diameter = max(self.diameter, left + right)

            # return height of current node
            return 1 + max(left, right)

        height(root)
        return self.diameter


if __name__ == "__main__":
    """
        Tree:
              1
             / \
            2   3
           / \
          4   5
    """

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    sol = Solution()
    ans = sol.diameterOfBinaryTree(root)

    print("Diameter of Binary Tree:", ans)
