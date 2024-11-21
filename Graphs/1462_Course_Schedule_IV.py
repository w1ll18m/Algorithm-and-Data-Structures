from typing import List
from collections import deque

class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:
        graph = [[] for _ in range(numCourses)]
        predecessor = [set() for _ in range(numCourses)]
        indegree = [0 for _ in range(numCourses)]

        # build the adjacency list representation of the graph and count the indegrees of each node
        for a, b in prerequisites:
            graph[a].append(b)
            indegree[b] += 1
        
        queue = deque()
        # intialize the queue with nodes with no prerequisites
        for node in range(numCourses):
            if indegree[node] == 0:
                queue.append(node)

        while len(queue) != 0:
            node = queue.popleft()

            # explore the neighbours
            for neighbour in graph[node]:
                # add current node's prerequisites and current node to neigbhour's prerequisites
                for prereq in predecessor[node]:
                    predecessor[neighbour].add(prereq)
                predecessor[neighbour].add(node)

                indegree[neighbour] -= 1
                # add neighbour to queue if all its prerequisites have been explored
                if indegree[neighbour] == 0:
                    queue.append(neighbour)

        # check all queries using the map of nodes and their prerequisites
        answer = [False for _ in range(len(queries))]
        for i in range(len(queries)):
            u, v = queries[i]
            if u in predecessor[v]:
                answer[i] = True
        
        return answer
        
    '''
    n courses (labeled from 0 to n - 1)
    prerequisites[i] = [ai, bi] indicates that you must take ai before taking bi
    a is a prerequisite of b if there is a path from a to b (THE GRAPH IS A TREE!!!)

    check if u is prerequisite of v in O(1) -> map node to set of prerequisites

    observe that if a -> b then the prerequisites of a are also the prerequisites of b
    thus we should build the prerequisite sets in topological order -> modified topological sort
        - topological sort is BFS but we keep track of in-degrees to explore nodes in topological order
        - for each neighbour, add the current node's prerequisites to the neighbour's prerequisites
        - NODES ARE ONLY PROCESSED ONCE ALL ITS PREDECESORS HAVE BEEN PROCESSED!!!
    '''
        