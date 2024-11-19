from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = [[] for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1
        
        queue = deque()
        topological_order = []

        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)
        
        while len(queue) != 0:
            node = queue.popleft()
            topological_order.append(node)

            for neighbour in graph[node]:
                indegree[neighbour] -= 1
                if indegree[neighbour] == 0:
                    queue.append(neighbour)
        
        if len(topological_order) == numCourses:
            return topological_order
        else:
            return []
    
    '''
    n courses (labeled from 0 to n - 1)
    prerequisites[i] = [ai, bi] which means you must take bi before ai
    return the ordering of courses you should take to finish all courses

    return a list such that for every prerequisite [a, b] then a occurs before b -> topological sort!
    O(n + m) time complexity where n is the # of courses and m is the # of prerequisites
    '''
        