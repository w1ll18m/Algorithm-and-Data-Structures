from typing import List

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        # construct the adjacency list representation of the graph
        graph = [[] for _ in range(n + 1)]
        for a, b, distance in roads:
            graph[a].append(b)
            graph[b].append(a)
        
        visited = set()

        def dfs(node):
            # check if node has been visited already
            if node in visited:
                return
            # add node to set of visited nodes
            visited.add(node)

            # explore the neighbours
            for neighbour in graph[node]:
                dfs(neighbour)
        
        # run DFS on node n to get all nodes in connected component
        dfs(n)

        # find the min weight edge where both end nodes are in the connected component
        min_score = float("inf")
        for a, b, distance in roads:
            if a in visited and b in visited and distance < min_score:
                min_score = distance
        
        return min_score
    
    '''
    n cities (1 to n)
    roads[i] = [ai, bi, distancei] indicates that there is a undirected edge between cities ai and bi with weight distancei
    path -> sequence of edges between 2 cities
        - a path can contain an edge multiple times -> we aren't dealing with shortest path
        - the score of a path is the lowest weight edge that it contains
    
    find the minimum score of a path between 2 cities -> explore all paths -> DFS/BFS?
    but since the path doesn't need to be shortest or have unique edges then we just need to find the edge with the lowest weight in the connected component -> DFS
    (1) call DFS on node n and keep track of all visited nodes
        - there is at least one path between 1 and n so they must be in the same connected component
    (2) iterate through the edges and find the minimum weight edge where both end nodes are in connected component
    thus total time complexity is O(n) for DFS and total space complexity is O(n + m) to store the adjacency list representation of the graph
    '''