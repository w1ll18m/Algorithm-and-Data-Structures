from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        parent = [i for i in range(n)]
        nofcomponents = n
        
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
            
            # if the edge is between 2 nodes of the same component then cycle detected
            if find(a) == find(b):
                return False
            # edge combines the two components
            union(a, b)
            nofcomponents -= 1
        
        return nofcomponents == 1
    
    '''
    n nodes (labeled from 0 to n - 1)
    edges[i] = [ai, bi] which indicates an undirected edge between ai and bi

    determine if these edges make up a valid tree -> check if cycle exists -> union find
    observe that adding an edge between 2 nodes in the same component will create a cycle
    so adding edge ab won't create a cycle if a and b are in different components

    checking if 2 nodes are in the same component -> check if find(x) == find(y)
    thus for each edge, we need to check if it will create a cycle
    total time complexity is O(n + m * a(n)) but total space complexity is O(n)
    '''
        