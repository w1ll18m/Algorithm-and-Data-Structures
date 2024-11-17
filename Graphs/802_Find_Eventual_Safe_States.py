from typing import List

class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        visited = [False for _ in range(n)]
        safe = [False for _ in range(n)]

        def dfs(i):
            if visited[i]:
                if safe[i]: return True
                else: return False

            visited[i] = True

            # case: node is a terminal
            if len(graph[i]) == 0:
                safe[i] = True
                return True
            
            isSafe = True
            # check if neighbours are safe/terminal nodes
            for neighbour in graph[i]:                
                isSafe = isSafe and dfs(neighbour)
            
            # if all neighbours are safe/terminal then current node is safe
            if isSafe:
                safe[i] = True
            return isSafe
        
        # iterate through entire graph and call DFS on unvisited nodes
        for i in range(n):
            if not visited[i]:
                dfs(i)
        
        safe_list = []
        for i in range(n):
            if safe[i]: safe_list.append(i)
        return safe_list
    
    '''
    directed graph with n nodes (labeled 0 to n - 1)
        - graph[i] is list of out neighbours of node i
    a node is a terminal node if there are no outgoing edges
    a node is a safe node if every possible path starting from that node leads to a terminal node (or another safe node)

    find all nodes that can reach the terminal node -> DFS/BFS
    want to check if all paths from a node leads to a safe node or terminal node (recursive) -> DFS
        - base: node is a terminal node then return True (and add to list of safe nodes)
        - otherwise: return True if all neighbours are safe/terminal nodes (add add to list of safe nodes)
        - need to maintain a list of visited nodes too
    thus total time complexity is O(n) and total space complexity is O(n) for storing (1) list of safe nodes
                                                                                      (2) list of visited nodes
    '''
        