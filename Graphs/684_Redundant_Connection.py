from typing import List

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        # trees have n nodes and n-1 edges so the transformed graph has n edges
        parent = [i for i in range(len(edges) + 1)]     # len(edges) + 1 since graph is 1-indexed

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
                return parent[x]
            else:
                return x
        
        def union(x, y):
            parent[find(y)] = find(x)
        
        for edge in edges:
            a, b = edge[0], edge[1]

            # if the edge is between 2 nodes in the same component then cycle detected
            if find(a) == find(b):
                return [a, b]
            
            # combine the 2 components connected by the edge
            union(a, b)
            
    '''
    undirected connected graph with no cycles -> tree
        - n nodes (labeled 1 to n)
    graph is transformed by adding one additional edge 
    return an edge that can be removed so that the resulting graph is a tree

    we want to detect a cycle in undirected graph -> DFS or Union Find
    (1) iterate through all of the edges
    (2) for each edge ab:
        (i) if a and b are in different components then combine the components
        (ii) if a and b are in same components then a cycle has been detected
            - return that edge as the answer
    observe that there is only 1 cycle and all edges in that cycle must already be added to the graph before the cycle detecting edge is encountered
    so the cycle detecting edge must be the last edge in the input in the cycle
    thus total time complexity is O(n + m * a(n)) but total space complexity is only O(n)
    '''
        