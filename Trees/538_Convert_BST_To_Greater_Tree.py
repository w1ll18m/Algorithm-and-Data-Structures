from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def convertBST(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        visited = []
        cur = root
        sum = 0

        while cur or len(visited) != 0:
            # case: right path not fully explored
            if cur:
                # add current node to the stack to be processed later
                visited.append(cur)
                # visit the right node
                cur = cur.right
            # case: right path is fully explored
            else:
                # process the current node
                cur = visited.pop()
                cur_val = cur.val
                cur.val += sum
                sum += cur_val
                # visit the left node
                cur = cur.left

        return root

    '''
    convert to a greater tree -> every key of BST is changed to key + sum of all keys greater than key
    
    given the smallest key, we will add the sum of all other keys
          the second smallest key, we will add the sum of all other keys (except for smallest key and itself)
          the third smallest key, we will add the sum of all other keys (except for smallest key, second smallest key, and itself)
          the largest key, we will add nothing because there are no keys greater
    observe that now the smallest key in BST is the largest key in the greater tree
                     the second smallest key in BST is the second largest key in the greater tree
                     [...]
                     the largest key in BST is the smallest key in the greater tree
    
    we need to traverse the entire tree -> right current left -> lets do this iteratively (use a stack)
    maintain a variable that keeps track of the sum of all the nodes visited thus far
    at each node: (1) add sum of all nodes thus far to current node
                  (2) add old key to the sum of all nodes thus far
    since we visit each node exactly once then total time complexity is O(n)
    '''
        