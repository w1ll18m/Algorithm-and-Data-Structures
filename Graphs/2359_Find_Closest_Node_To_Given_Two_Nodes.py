from typing import List
from collections import deque

class Solution:
    def closestMeetingNode(self, edges: List[int], node1: int, node2: int) -> int:
        distance1 = [float('inf') for _ in range(len(edges))]
        distance2 = [float('inf') for _ in range(len(edges))]
        queue = deque()

        # run BFS on node1
        distance1[node1] = 0
        queue.append(node1)

        while len(queue) != 0:
            node = queue.popleft()
            neighbour = edges[node]
            if neighbour != -1 and distance1[neighbour] == float('inf'):
                distance1[neighbour] = distance1[node] + 1
                queue.append(edges[node])
        
        # run BFS on node 2
        distance2[node2] = 0
        queue.append(node2)

        while len(queue) != 0:
            node = queue.popleft()
            neighbour = edges[node]
            if neighbour != -1 and distance2[neighbour] == float('inf'):
                distance2[neighbour] = distance2[node] + 1
                queue.append(edges[node])

        # iterate and compare the distance vectors of both nodes
        smallest = (0, max(distance1[0], distance2[0]))
        for i in range(1, len(edges)):
            path_max = max(distance1[i], distance2[i])
            if path_max < smallest[1]:
                smallest = (i, path_max)
        
        if smallest[1] != float('inf'):
            return smallest[0]
        else:
            return -1

    '''
    directed graph of n nodes (0 to n - 1) where each node has at most 1 out edge
    find node with smallest distance to either node1 or node2 -> BFS

    (1) run BFS on node1 and keep track of distance from node1 to all other nodes
    (2) run BFS on node2 and keep track of distance from node2 to all other nodes
    (3) iterate and compare the distance vectors of both nodes to find the node with the smallest distance to either node1 or node2
    thus total time complexity is O(n) for BFS and total space complexity is O(n) to store distance vectors
    '''
        