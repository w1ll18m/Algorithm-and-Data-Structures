from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        def updateSet(val, odd_set):
            if val not in odd_set:
                odd_set.add(val)
            else:
                odd_set.remove(val)

        def countPalindromic(node, digits):    
            # if node is None then return 0 (is not a root-leaf path)
            if node is None:
                return 0

            # update the even/odd status of current node's digit in the map
            updateSet(node.val, digits)
            
            # if node is a leaf node then check if path is pseudo palindromic
            if not node.left and not node.right:
                if len(digits) < 2:
                    # restore hashmap to state before current digit is added
                    updateSet(node.val, digits)
                    return 1
                else:
                    updateSet(node.val, digits)
                    return 0
            
            # recurse to find # of pseudo-palindromic paths in left and right subtrees
            nofleft = countPalindromic(node.left, digits)
            nofright = countPalindromic(node.right, digits)

            updateSet(node.val, digits)
            return nofleft + nofright
        
        return countPalindromic(root, set())

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

    can we improve the time complexity? -> YES!!!
    checking hashmap takes O(n) is prev solution which is why the solution takes O(n * h) time complexity
    we only care about odd and even -> set with odd digits
        - if digit is not in set then its count is currently even
            - now it is odd so add digit to set
        - if digit is in set then its count is currently odd
            - now it is even so remove digit from set
        - if length of set > 1 then we have more than one odd digit
            - we can check the length of the hashmap in O(1) time
    how do we ensure O(n) space complexity?
        - instead of removing digit from map before recursive return
        - update the set again (reverses the changes)
    thus total time complexity is O(n) and space complexity is O(n)
    '''