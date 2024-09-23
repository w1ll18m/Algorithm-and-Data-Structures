from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        if root is None:
            return ""
        
        # recursively compute string representations of left and right subtrees
        left_str = self.tree2str(root.left)
        right_str = self.tree2str(root.right)

        # omit empty parenthesis pairs by checking cases
        if right_str != "":
            return f"{root.val}({left_str})({right_str})"
        elif left_str != "":
            return f"{root.val}({left_str})"
        else:
            return f"{root.val}"
    
    '''
    create a pre-order string representation for a tree -> current node, left subtree, right subtree

    each node in the tree is represented by its integer value
    children should be represented in parentheses:
        - return cur.val + "(" + dfs(left) + ")" + "(" + dfs(right) + ")"
    omit empty parenthesis pair (unless node has right child but no left child):
        - check values of dfs(left) and dfs(right)
        - if dfs(left) == dfs(right) == "" THEN return cur.val
        - if dfs(left) != "" but dfs(right) == "" THEN return cur.val + "(" + dfs(left) + ")"
        - if dfs(right) != "" THEN return cur.val + "(" + dfs(left) + ")" + "(" + dfs(right) + ")"
    '''