from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = [[] for _ in range(n)]
        visited = [False for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(i):
            if visited[i]:
                return
            visited[i] = True

            for neighbour in graph[i]:
                dfs(neighbour)
        
        nofcomponents = 0
        for node in range(n):
            if not visited[node]:
                dfs(node)
                nofcomponents += 1
        
        return nofcomponents