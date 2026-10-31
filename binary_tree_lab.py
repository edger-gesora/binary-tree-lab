from typing import Optional

class TreeNode:
    def __init__(self, val: int):
        self.val = val
        self.left: Optional['TreeNode'] = None
        self.right: Optional['TreeNode'] = None

# TODO: Implement the max_depth function
def max_depth(root: Optional[TreeNode]) -> int:
    """
    Determine the maximum depth (height) of a binary tree.
    Uses recursion to compute left and right subtree depths and returns the max + 1.
    """
    # Base case: if the node is empty, depth is 0
    if not root:
        return 0
    
    # Recursively find the depth of left and right subtrees
    left_depth = max_depth(root.left)
    right_depth = max_depth(root.right)
    
    # Return the maximum depth plus one for the current root node
    return max(left_depth, right_depth) + 1

# TODO: Implement the lowest_common_ancestor function
def lowest_common_ancestor(root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
    
    """
    Find the lowest common ancestor (LCA) of two nodes in a Binary Search Tree (BST).
    Utilizes BST properties to navigate left/right appropriately.
    """
    current = root
    
    while current:
        # If both p and q are smaller than the current node, LCA lies in the left subtree
        if p.val < current.val and q.val < current.val:
            current = current.left
        # If both p and q are greater than the current node, LCA lies in the right subtree
        elif p.val > current.val and q.val > current.val:
            current = current.right
        else:
            # We have found the split point, which is the LCA
            return current