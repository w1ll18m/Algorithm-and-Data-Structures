from typing import List
from collections import deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for prerequisite in prerequisites:
            a, b = prerequisite[0], prerequisite[1]
            # create the adjacency list representation of the graph
            graph[a].append(b)
            # keep track of the in-degree of each node
            indegree[b] += 1

        queue = deque()
        topological_order = []

        # intialize the queue with nodes with in-degree of 0
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        while len(queue) != 0:
            # process the current node
            node = queue.popleft()
            topological_order.append(node)

            # explore the neighbours
            for neighbour in graph[node]:
                # decrement the in-degree of neighbours
                indegree[neighbour] -= 1
                # add neighbours with in-degree of 0 to processing queue
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        return len(topological_order) == numCourses

    '''
    n courses (labeled 0 to n - 1) that you have to take
    prerequisites[i] = [ai, bi] indicates that you have to take bi before taking ai
    return True if you can finish all the courses

    we want to determine if there is a cycle in the directed graph -> check if topological ordering exists
    need to construct adjacency list representation of graph -> O(n) time

    topological sort (BFS) -> sorts the tree/forest such that for every edge u -> v, vertex u appears before vertex v
        - key idea: we want to process nodes with no in-neighbours first (and then the next level of nodes)
            - construct a map of nodes to their in-degrees -> O(n)

        (1) initialize a queue and add all nodes with in-degree = 0 
            - in-degree = 0 indicates that the node has no dependencies that need to be processed first

        (2) while queue is not empty then pop a node
            - process this node by adding it to the topological order list
            - decrement in-degree of all neighbours (since one of their dependencies has been processed)
            - if any neighbour has in-degree = 0 then it is ready to be processed so add it to the queue
    
    key idea (for cycle detection): nodes in a cycle will always have in-degree >= 0
        - it will never be processed in topological sort 
        - thus the length of topological order list will be less than n
    '''
        