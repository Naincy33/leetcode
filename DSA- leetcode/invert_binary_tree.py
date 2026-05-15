# Definition of Tree Node
class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None


# Function to invert binary tree
def invertTree(root):
    if root is None:
        return None

    # swap left and right
    root.left, root.right = root.right, root.left

    # recursive calls
    invertTree(root.left)
    invertTree(root.right)

    return root


# Inorder traversal (to verify result)
def inorder(root):
    if root is None:
        return
    inorder(root.left)
    print(root.val, end=" ")
    inorder(root.right)


if __name__ == "__main__":
    """
        Original Tree:
              4
             / \
            2   7
           / \ / \
          1  3 6  9
    """

    root = TreeNode(4)
    root.left = TreeNode(2)
    root.right = TreeNode(7)
    root.left.left = TreeNode(1)
    root.left.right = TreeNode(3)
    root.right.left = TreeNode(6)
    root.right.right = TreeNode(9)

    print("Inorder before invert:")
    inorder(root)

    invertTree(root)

    print("\nInorder after invert:")
    inorder(root)
