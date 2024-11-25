from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        parent = [i for i in range(n)]
        nofcomponents = n

        def find(x):
            if parent[x] == x:
                return x
            else:
                parent[x] = find(parent[x])
                return parent[x]
        
        def union(x, y):
            parent[find(y)] = parent[find(x)]
        
        for edge in edges:
            x, y = edge[0], edge[1]
            if find(x) != find(y):
                nofcomponents -= 1
                union(x, y)

        return nofcomponents

    '''
    # of connected components -> DFS O(n + m) or Union Find O(m)

    connected component = group of elements with edges
    # of connected components = # of groups of elements with edges
    (1) iterate through all the edges
    (2) for edge x, y, if x and y aren't in the same group then combine them
    
    thus the total time complexity is O(n + m * a(n)) but the total space complexity is O(n)

    Union Find: 
        - every group of elements is a tree (with a root node)
        - find(x) returns the root of the tree that element x is part of 
            - traverse UP the tree with parent array (root has parent[x] = x)
            - 2 elements are in the same group if find(x1) = find(x2)
        - union(x, y) combines two disjoint groups of elements
            - set parent of the root of group y to the root of group x
            - parent[find(y)] = find(x)
    
    parent = [i for i in range(n)]

    O(a(n)) where a(n) grows EXTREMELY slowly and is effectively constant (with path compression)
    find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])
            return parent[x]
        else:
            return x
    
    O(a(n))
    union(x, y):
        parent[find(y)] = parent[find(x)]
    '''

        