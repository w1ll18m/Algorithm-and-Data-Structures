from typing import List

class Solution:
    def findSmallestSetOfVertices(self, n: int, edges: List[List[int]]) -> List[int]:
        # traverse through edges and construct mapping of node to indegree
        indegree = [0 for _ in range(n)]
        for a, b in edges:
            indegree[b] += 1

        # find the nodes in the mapping with an indegree of 0
        smallest_set = []
        for i in range(len(indegree)):
            if indegree[i] == 0:
                smallest_set.append(i)

        return smallest_set
    
    '''
    directed acyclic graph with n nodes (0 to n-1) -> TREE!!!
    edges[i] = [ai, bi] represents a directed edge from node ai to node bi

    find the smallest set of vertices from which all nodes in the graph are reachable
    find all the source nodes (can not be reached from another node) in topological order -> find all nodes with indegree of 0
    (1) traverse through edges and construct mapping of node to indegree 
    (2) return the nodes in the mapping with an indegree of 0
    thus total time complexity is O(n + m) and total space complexity is O(n)
    '''