from typing import List

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # build the graph structure
        graph = [[] for _ in range(numCourses)]
        for a, b in prerequisites:
            graph[a].append(b)

        # all nodes are unvisited to begin with
        visited = [False for _ in range(numCourses)]
        # maintain a stack representing nodes in the current path
        path = set()

        def DFS(node):
            # check if the node is already in the path (loop detected)
            if node in path: return False
            # check if the node has already been visited
            if visited[node]: return True

            # add the current node to the path
            path.add(node)

            isTree = True
            # recursively explore all paths from current node
            for neighbour in graph[node]:
                isTree = DFS(neighbour) and isTree
            
            # remove the current node from the path
            path.remove(node)
            # mark the node as visited
            visited[node] = True
            
            return isTree
        
        for i in range(numCourses):
            if not visited[i] and not DFS(i):
                return False
        
        return True

    '''
    prerequisites[i] = [ai, bi] -> indicates that you must take course bi before ai
        - return true if you can finish all courses

    suppose that each course represents a node on the graph -> determine if the graph is a tree (no cycles) -> DFS? union find? topological sort?
        - union find can only detect cyles in an undirected graph
        - topological sort -> produces a DAG -> if len(DAG) != n then there is a cycle
        - recursive DFS -> maintain a set of elements in the current path
            - explore all paths at each given node -> visit all unvisited neighbour nodes
                - only mark a node as visited if we are done checking all its paths
            - maintain a set of elements in the current path -> visiting a node in that set means there is a cycle!!!
            - call DFS to visit all nodes
    
    thus total time complexity is O(n) since we visit each node exactly once
    '''
        