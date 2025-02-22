from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        # build the graph and indegree map
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]
        for a, b in prerequisites:
            # edge is b -> a
            graph[b].append(a)
            indegree[a] += 1

        # initialize queue with nodes with indegree of 0
        queue = deque()
        for i in range(numCourses):
            if indegree[i] == 0:
                queue.append(i)
        
        topological_order = []
        # process each node with indegree of 0
        while len(queue) != 0:
            node = queue.popleft()
            topological_order.append(node)
            
            # decrement indegree of out neighbours
            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                # add neighbour to queue if it has indegree of 0
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # if length of topological array is less than n then there is a cycle
        if len(topological_order) != numCourses:
            return []
        
        return topological_order
    
    '''
    prerequites[i] = [ai, bi] indicates that you need to take course b to take course a
    return the order of courses you should take to finish all courses -> topological order!!!

    topological sort
    (1) build the graph -> O(n) time complexity
    (2) map each node to its indegree -> O(n) time complexity (can be done when building the graph)
    (3) create a queue to store nodes with indegree of 0
        - indegree of 0 indicates that all its dependencies have already been processed
        - initialized with nodes with zero in-edges -> O(n) to iterate through indegree map
    (4) process the current node
        - add the current node to the topological order array
        - decrement indegree of all out neighbours
    (5) if len(topological_order_array) < numCourses then the graph is not a valid tree -> return empty array

    thus total time complexity is O(n) since we visit each node exactly once
    '''
        