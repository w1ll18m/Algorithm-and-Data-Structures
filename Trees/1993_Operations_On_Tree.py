from typing import List

class LockingTree:

    def __init__(self, parent: List[int]):
        # keep track of parent array
        self.parent = parent

        # create map of node to user (initialize values with -1 to show that they are all unlocked)
        self.locks = {}
        for i in range(len(parent)):
            self.locks[i] = -1
        
        # create map of node to children
        self.tree = {}
        for i in range(len(parent)):
            self.tree[i] = []
        for i in range(len(parent)):
            if parent[i] != -1:
                self.tree[parent[i]].append(i)

    def lock(self, num: int, user: int) -> bool:
        # check if node is unlocked
        if self.locks[num] == -1:
            # lock the node for the user
            self.locks[num] = user
            return True
        else:
            return False

    def unlock(self, num: int, user: int) -> bool:
        # check if node is locked by user
        if self.locks[num] == user:
            # unlock the node
            self.locks[num] = -1
            return True
        else:
            return False

    def upgrade(self, num: int, user: int) -> bool:
        # check if node is unlocked
        if self.locks[num] != -1:
            return False
        
        # check if ancestor nodes are unlocked
        cur = self.parent[num]
        while cur != -1:
            # check if current ancestor node is locked
            if self.locks[cur] != -1:
                return False
            # traverse to the next ancestor node
            cur = self.parent[cur]
        
        # check if descendants are locked (and unlock any that are locked)
        self.hasLocked = False  # keep track if any descendants are locked

        def checkAndUnlock(node):
            # check if current descendant node is locked
            if self.locks[node] != -1:
                self.hasLocked = True
                # unlock the descendant node
                self.locks[node] = -1
            
            # recurse on descendants
            for child in self.tree[node]:
                checkAndUnlock(child)
        
        checkAndUnlock(num)
        # if a descendant node was unlocked then lock the node
        if self.hasLocked:
            self.locks[num] = user
        return self.hasLocked

'''
given a tree with n nodes (0 to n-1)
parent[i] is the parent of the ith node
the root of the tree is 0
    - parent[0] = -1

observe that we can traverse the tree from a node to the root using parent
we can also construct a hashmap that maps a node to its children (int -> List[int])
    - iterate through the parent
    - if parent[i] = j then map[j].append(i)

lock -> (1) lock the node for a given user (only if node is unlocked)
        (2) prevents other users from locking the same node
    - returns true if it is possible to lock and then locks the node
    - returns false otherwise
we can use another hashmap that maps a node to a user (int -> int)
    - use -1 to represent that a node is unlocked

unlock -> (1) unlock the node (only if user currently locks it)
    - returns true if it is possible to unlock and then unlocks it
    - returns false otherwise

upgrade -> (1) locks the given node for the given user (check if unlocked using hashmap)
           (2) check for locked ancestors (traverse parent array)
           (3) check and unlock descendants (traverse children hashmap)
    - returns true if it is possible to upgrade and then upgrades it
    - returns false otherwise
'''

# Your LockingTree object will be instantiated and called as such:
# obj = LockingTree(parent)
# param_1 = obj.lock(num,user)
# param_2 = obj.unlock(num,user)
# param_3 = obj.upgrade(num,user)