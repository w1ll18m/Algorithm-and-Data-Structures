from typing import List
from collections import deque

class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: List[List[int]], blueEdges: List[List[int]]) -> List[int]:
        # intialize the distance vector and visited sets
        answer = [-1 for _ in range(n)]
        redVisited = [False for _ in range(n)]      # redVisited[i] = True means node where next edge is red has been visited
        blueVisited = [False for _ in range(n)]     # blueVisited[i] = True means node where next edge is blue has been visited

        # construct the graph (first list is red neighbours and second list is blue neighbours)
        graph = [([], []) for _ in range(n)]

        for a, b in redEdges:
            graph[a][0].append(b)
        for u, v in blueEdges:
            graph[u][1].append(v)

        # intialize the queue with the source node (need to consider both red and blue edges)
        queue = deque()
        queue.append((0, 0, 0))    # 0 indicates that next edge needs to be red, 0 is the current path length
        redVisited[0] = True
        queue.append((0, 1, 0))    # 1 indicates that next edge needs to be blue, 0 is the current path length
        blueVisited[0] = True
        answer[0] = 0
        
        while len(queue) != 0:
            node, colour, path = queue.popleft()

            # if next edge needs to be red then explore the red neighbours
            if colour == 0:
                for neighbour in graph[node][0]:
                    # visit all neighbours that have not already been visited via a red edge
                    if not blueVisited[neighbour]:
                        queue.append((neighbour, 1, path + 1))
                        blueVisited[neighbour] = True

                        # only update distance vector if current path is shorter
                        if answer[neighbour] == -1 or path + 1 < answer[neighbour]:
                            answer[neighbour] = path + 1

            # if next edge needs to be blue then explore the blue neighbours
            else:
                for neighbour in graph[node][1]:
                    # visit all neighbours that have not already been visited via a blue edge
                    if not redVisited[neighbour]:
                        queue.append((neighbour, 0, path + 1))
                        redVisited[neighbour] = True

                        # only update distance vector if current path is shorter
                        if answer[neighbour] == -1 or path + 1 < answer[neighbour]:
                            answer[neighbour] = path + 1
        
        return answer

    '''
    directed graph of n nodes (0 to n-1)
    each edge is either red or blue (there can be self-edges and parallel edges)
    redEdges[i] = [ai, bi] indicates theres a directed red edge from node ai to bi (similar for blueEdges)
    return shortest path from 0 to all other paths such that edge colors alternate along the path -> modified BFS

    self-edges and parallel edges -> revisit node at most once (to swap colors) -> maintain 2 visited sets (one for red and blue)
    need to keep track of color of the previous edge
        - source node 0 has no incoming edge so we can visit red edges and blue edges
    since we may a node twice then we should only update its distance if its shorter

    thus total time complexity is O(n + m) for BFS and total space complexity is O(n) to store visited sets and BFS queue

    ALTERNATIVELY (but similarily) -> use 1 visited set but treat (node, red) and (node, blue) as seperate nodes
    '''
        