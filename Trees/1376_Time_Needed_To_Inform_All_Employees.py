from typing import List

class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        manager_tree = {}
        for i in range(n):
            manager_tree[i] = []
        
        # build the hash map: manager -> [subordinates]
        for i in range(len(manager)):
            employee = i
            boss = manager[i]
            if boss != -1:
                manager_tree[boss].append(employee)
        
        # recursively calculate the longest path
        def getLongestPath(rootID):
            # if informTime[i] == 0 then no subordinates
            if informTime[rootID] == 0:
                return 0
            
            longest_path = 0
            # get the list of subordinates of the current manager
            subordinates = manager_tree[rootID]
            # recurse on subordinates to get longest path of subtrees
            for subordinate in subordinates:
                path = getLongestPath(subordinate)
                if path > longest_path:
                    longest_path = path
            
            # add informTime of current manager to the longest path of subtrees
            longest_path += informTime[rootID]
            return longest_path
        
        return getLongestPath(headID)
                
    '''
    n employees with unique IDs from [0, n-1], headID is the head of the company
    manager[i] is the direct manager of the i-th employee
        - manager[headID] = -1
    
    the number of minutes needed to inform all employees -> longest path in the tree
    how can we check who is managed by an employee?
        - create a hash map: manager_id -> [subordinates]
    then we can recursively calculate the longest path:
        - get the list of subordinates of the current manager_id from the hashmap
        - recurse on subordinates to get longest path of its subtree
        - add informTime[manager_id] to longest path of its subtree
    observe that we visit each node exactly once hence time complexity is O(n)
    '''