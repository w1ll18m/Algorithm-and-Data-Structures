from typing import List
from collections import defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # construct the graph
        graph = defaultdict(list)
        for i in range(len(equations)):
            a, b = equations[i]
            graph[a].append((b, values[i]))
            graph[b].append((a, 1 / values[i]))

        def answer_query(start, end):
            visited = set()

            def dfs(node, path_score):
                # if node has been visited then this path is not valid
                if node in visited:
                    return (False, path_score)
                # if node is the end node then this path is valid
                if node == end:
                    return (True, path_score)
                visited.add(node)

                # explore the neighbours
                if node in graph:
                    for neighbour, weight in graph[node]:
                        # follow the edge to the neighbour and update path score
                        path_exists, score = dfs(neighbour, path_score * weight)

                        # if following the edge leads to a valid path then return the score of the path
                        if path_exists:
                            return (True, score)

                # not path visiting this node is valid
                return (False, path_score)
            
            path_exists, score = dfs(start, 1)

            return (path_exists, score)
        
        answer = [-1 for _ in range(len(queries))]
        for i in range(len(queries)):
            c, d = queries[i]
            path_exists, score = answer_query(c, d)

            if c in graph and d in graph and path_exists:
                answer[i] = score

        return answer
    
    '''
    equations[i] = [Ai, Bi] and values[i] represents an equation Ai / Bi = values[i]
    queries[j] = [Cj, Dj] represents the jth query that you need to find the answers for
    return the answer to all queries (find the value of all cj / dj)
    hint: do you recognize this as a graph problem? -> lol no

    suppose that each variable represents a node -> equations[i] represents a directed edge from ai to bi
    instead of explicitly calculating the values of each equation, lets calculate it implicitly
        - suppose a/b = 2 and b/c = 3 then a/c = a/b * b/c = 2 * 3 = 6
        - suppose a/b = 2 and b/c = 3 then c/a = b/a * c/b = 1/2 * 1/3 = 1/6
    thus we can answer cj / dj by finding a path (multiplying edge weights) between cj and dj
    where the weight of each edge [ai, bi] = values[i] and [bi, ai] = 1 / values[i]

    to answer a given query -> perform DFS to find and return the value of a path
    thus total time complexity is O(n * m) where n is the # of equations and m is the # of queries
    '''