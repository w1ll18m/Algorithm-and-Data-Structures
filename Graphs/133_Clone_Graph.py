from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        cloned = {}
        visited = set()     # NOT NEEDED SINCE WE ADD VISITED NODES TO CLONED!!!

        def cloneNode(node):
            # mark the cell as visited
            visited.add(node.val)

            # make a clone of the node while leaving neighbors empty
            cloned_node = Node(node.val)
            cloned_neighbors = []
            cloned[node.val] = cloned_node  # map node.val to cloned node

            # explore the neighbors
            for neighbor in node.neighbors:
                # check if neighbor has already been cloned
                if neighbor.val in cloned:
                    cloned_neighbors.append(cloned[neighbor.val])
                else:
                    # clone the neighbor and add it to adj list
                    cloned_neighbor = cloneNode(neighbor)
                    cloned_neighbors.append(cloned_neighbor)

            cloned_node.neighbors = cloned_neighbors
            
            return cloned_node
        
        if node is None:
            return None
        return cloneNode(node)

    '''
    deep copy of the graph (could contain cycles) -> hashmap of node.val to cloned node
    we need to explore every single node -> DFS
        - use a set to maintain a list of nodes (their values) that have been visited
    for each node:
        - make a clone of the node (leave neighbous empty)
        - need to clone every neighbor node and add it to the adj list
            - case 1: neighbor is already cloned then find its clone using hashmap
            - case 2: neighbor is not cloned then recurse 
            - hashmap allows us to check if a neighbor is cloned and find its clone in O(1) time
    since we visit each node exactly once and we iterate through adj list then worst case time complexity is O(n^2)
    '''