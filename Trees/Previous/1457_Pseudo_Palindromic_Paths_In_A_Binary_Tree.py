from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def checkPalindrome(dictionary):
            hasOdd = False
            for key, val in dictionary.items():
                if val % 2 == 1:
                    if hasOdd: return False
                    else: hasOdd = True
            return True

        def countPalindromic(node, digits):    
            # if node is None then return 0 (is not a root-leaf path)\
            if node is None:
                return 0

            # add the current node's digit to the map
            if node.val not in digits:
                digits[node.val] = 1
            else:
                digits[node.val] += 1
            
            # if node is a leaf node then check if path is pseudo palindromic
            if not node.left and not node.right:
                if checkPalindrome(digits):
                    # remove digit from map (since its passed by value)
                    digits[node.val] -= 1
                    return 1
                else:
                    digits[node.val] -= 1
                    return 0
            
            # recurse to find # of pseudo-palindromic paths in left and right subtrees
            nofleft = countPalindromic(node.left, digits)
            nofright = countPalindromic(node.right, digits)

            digits[node.val] -= 1
            return nofleft + nofright
        
        return countPalindromic(root, {})

    '''
    return the # of pseudo-palindromic paths
    need to explore all nodes -> DFS + pass information about ancestor nodes

    how do we pass information about ancestor nodes?
        - we can pass a hashmap with digit -> count
            - need to remove digit from map before recursive return to ensure O(n) space complexity
            - at each leaf, check if hashmap represents a valid a palindrome
                - if all counts are even (with at most one odd) then it represents a valid palindrome
                - check has O(n) time complexity
                - since there are at most 2h - 1 leaves then total time complexity is O(n * h)
    thus total time complexity is O(n * h) and space complexity is O(n)
    '''