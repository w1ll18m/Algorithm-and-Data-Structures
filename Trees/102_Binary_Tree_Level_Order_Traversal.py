import queue

# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def levelOrder(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        nextq = queue.Queue()
        if root:
            nextq.put(root)
        level_order = []

        while not nextq.empty():
            level = []

            for i in range(nextq.qsize()):
                curnode = nextq.get()
                level.append(curnode.val)
                if curnode.left:
                    nextq.put(curnode.left)
                if curnode.right:
                    nextq.put(curnode.right)
            
            level_order.append(level)
        
        return level_order
    
    '''
    using collection.deque() might be faster than using queue.Queue()
    '''


        