from typing import List
from collections import deque

class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        # visited[0] is set A and visited[1] is set B
        visited = [[False for _ in range(len(graph))], [False for _ in range(len(graph))]]
        
        def bfs(node):
            # intialize the queue and assign the starting node to set A
            queue = deque()
            queue.append(node)
            visited[0][node] = True

            while len(queue) != 0:
                cur = queue.popleft()
                cur_set = int(visited[1][cur] == True)
                opp_set = 1 - cur_set

                # explore the neighbours
                for neighbour in graph[cur]:
                    # check if neighbour is in the same set as the current node
                    if visited[cur_set][neighbour]: return False
                    # check if neighbour is in the opposite set as the current node
                    if visited[opp_set][neighbour]: continue
                    
                    # assign the neighbour to the opposite set and add it to the queue
                    visited[opp_set][neighbour] = True
                    queue.append(neighbour)
            
            return True
        
        # check if all connected components are bipartite
        for i in range(len(graph)):
            if not visited[0][i] and not visited[1][i]:
                if not bfs(i): return False
        
        return True

    '''
    undirected graph with n nodes (0 to n - 1) -> graph is an adjacency list representation
        - there are no self edges or parallel edges
        - the graph may not be connected
    bipartite -> nodes partitioned into 2 independent sets where every edge connects a node in A to B

    observe that a graph is bipartite if it is 2-colourable -> DFS/BFS
    (1) maintain 2 sets that represent node A and node B respectively (these will act as our visited set too)
    (2) start BFS at any given node and assign it to set A
    (3) for each node, (i)   check which set it belongs to
                       (ii)  assign neighbour to opposite set if it is not in any sets and add it to the queue
                       (iii) if the neighbour is in the opposite set already then do nothing
                       (iv)  if the neighbour is in the same set already then an edge between 2 nodes in the same set has occured so graph is not bipartite
    thus total time complexity is O(n + m) while total space complexity is O(n) to maintain the 2 sets
    '''
        