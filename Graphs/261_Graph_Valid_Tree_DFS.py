from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        graph = [[] for _ in range(n)]
        visited = set()
        path = set()

        # build the adjacency list representation
        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)
        
        def dfs(node, parent):
            if node in visited:
                # check if visited node is in current path
                if node in path: return False
                else: return True
            
            visited.add(node)
            path.add(node)
            
            isValid = True
            # explore the neighbours
            for neighbour in graph[node]:
                if neighbour != parent:
                    isValid = dfs(neighbour, node) and isValid
            
            # done exploring node's paths so remove it from the current path
            path.remove(node)

            return isValid
        
        # check if all connected components don't contain cycles
        nofcomponents = 0
        for node in range(n):
            if node not in visited:
                if not dfs(node, -1):
                    return False     
                nofcomponents += 1
        
        # need to check if the graph is a forest or a tree
        if nofcomponents == 1: return True
        else: return False

    '''
    n nodes (labeled from 0 to n - 1)
    edges[i] = [ai, bi] which indicates an undirected edge between ai and bi

    determine if these edges make up a valid tree -> check if cycle exists
    a graph has a cycle if any path visits a node more than once
    check if all paths in the graph don't visit a node more than once -> DFS

    use a set to keep track of what nodes have been visited in the current path
        - add node to set when we first visit it and remove it when we are done processing it
        - what happens if the neighbour has been visited? -> check if its in the current path
            - if it exists in the current path then there's a cycle
            - if it does not exist then we have already checked all paths starting from that node
    
    how do we avoid taking the undirected edge back to the parent? -> pass in the parent as an argument of DFS
    
    thus total time complexity is O(n + m) to perform DFS
    and total space complexity is O(n + m) to maintain the adjacency list representation of the graph
    '''
        