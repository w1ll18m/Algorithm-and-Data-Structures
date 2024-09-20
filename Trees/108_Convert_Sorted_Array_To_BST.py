from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def sort(nums, start, end):
            if start > end:
                return None

            middle = (start + end) // 2

            left_tree = sort(nums, start, middle - 1)
            right_tree = sort(nums, middle + 1, end)
            return TreeNode(nums[middle], left_tree, right_tree)
        
        return sort(nums, 0, len(nums) - 1)

    '''
    elements are stored in ascending order -> [0, 1, 2, 3, 4, 5]
    we want to convert it to a height-balanced binary search tree

    if we want a height-balanced tree, we need half the nodes on the left and the other half on the right
        - elements are sorted so the middle element has half of the elements on each side
        - (start + end) // 2
    so build a recursive function that lets the middle element be the root and builds the tree recursively from left/right sides
    '''
        