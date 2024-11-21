from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        # return the # of nodes and edges in the connected component
        def dfs(node):
            if node in visited:
                # already contributed to node count but contributes 1 to edge count
                return (0, 1)
            visited.add(node)

            nofnodes, nofedges = 1, 0
            # explore the neighbours
            for neighbour in graph[node]:
                k, e = dfs(neighbour)
                nofnodes += k
                nofedges += e
            
            return nofnodes, nofedges
        
        # check if all connected components are valid trees by comparing # of nodes and edges
        for node in range(n):
            if node not in visited:
                k, e = dfs(node)
                if not e == n - 1:
                    return False
        
        return True

    '''
    n nodes (labeled from 0 to n - 1)
    edges[i] = [ai, bi] which indicates an undirected edge between ai and bi

    determine if these edges make up a valid tree -> check if cycle exists
    valid tree -> there are exactly n-1 edges
    valid forest -> each connected component of size k has exactly k-1 edges
    explore every component and count # of edges and nodes -> DFS
    thus total time complexity is O(n + m)
    and total space complexity is O(n + m) to maintain adjacency list representation
    '''
        