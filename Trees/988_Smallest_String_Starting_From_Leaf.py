from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # use list since we can modify list in checkPathStrings function
        smallest_string = [chr(26 + ord('a'))]

        def checkPathStrings(node, ancestor_string):
            if node.left is None and node.right is None:
                # add current node's character to the string
                path_string = chr(node.val + ord('a')) + ancestor_string
                # check if leaf-root string is smaller than smallest string so far
                if path_string < smallest_string[0]:
                    smallest_string[0] = path_string
                return
            
            # add current node's character to the string
            path_string = chr(node.val + ord('a')) + ancestor_string
            # recurse on left/right subtrees
            if node.left: checkPathStrings(node.left, path_string)
            if node.right: checkPathStrings(node.right, path_string)
        
        checkPathStrings(root, "")
        return smallest_string[0]
    
    '''
    return the lexicographically smallest string (starting at leaf and ending at root)
    we need to traverse the entire tree -> DFS (+ pass information about ancestors)

    lets come up with a recursive solution:
        - if node is None then return an empty string ""
        - if node is Leaf then return chr(node.val + ord('a'))
        - if node is not a Leaf then
            - recurse on left/right subtrees to find smallest string ending at left/right children
            - return smallest_subtree_string + chr(node.val + ord('a')) 
    since we visit each node exactly once and string operations are O(n) time then total time complexity is O(n^2)

    to avoid comparing strings at every node, we can define our recursive solution to only compare strings at leaf nodes
    maintain a variable that keeps track of the smallest string so far
    lets come up with an improve recursive solution:
        - we need to pass in string formed by ancestors as parameter
        - if node is Leaf then check if chr(node.val + ord('a')) + ancestor_string is smaller than smallest string so far
        - if node is not a Leaf then recurse on non empty children
    since we visit each node exactly once and string operations only occur at Leaf then total time complexity is O(n + n * h) = O(n * h)
        - there are at most 2h + 1 leaves in a tree (balanced tree)
    '''
        