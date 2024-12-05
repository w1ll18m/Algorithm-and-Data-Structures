from typing import List
from collections import defaultdict

class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        outedges = defaultdict(list)
        inedges = defaultdict(list)

        # construct the in-edges and out-edges representation of the graph
        for a, b in connections:
            outedges[a].append(b)
            inedges[b].append(a)
        
        visited = [False for _ in range(n)]
        def dfs(node):
            visited[node] = True
            
            count = 0
            # explore the neighbour
            for neighbour in outedges[node]:
                # increment count for every directed edge to an unvisted neighbour
                if not visited[neighbour]:
                    count += 1
                    count += dfs(neighbour)
            for neighbour in inedges[node]:
                if not visited[neighbour]:
                    count += dfs(neighbour)

            return count

        # start DFS at capital (0)
        return dfs(0)

    '''
    n cities (0 to n - 1)
    n - 1 roads (aka directed edges) where there is only one road between 2 cities -> tree
    connections[i] = [ai, bi] represents an edge from ai to bi
    return the # of roads that need to be reordered to ensure that all cities can reach city 0

    observe that a tree with directed edges must be a tree even if its edges were undirected
    any node that can be reached starting from the capital (0) can not reach the capital itself -> DFS from 0
        - need to traverse in-edges too since there might be out-edges that can't be directly reached from the capital (don't count these)
        - count the # of out-edges taken (corresponds to # of edges needed to flip)

    thus total time complexity is O(n + m) to construct the in-edge and out-edge representation of the graph + DFS from 0
    thus total space complexity is O(n + m) to store the in-edge and out-edge representation of the graph
    '''