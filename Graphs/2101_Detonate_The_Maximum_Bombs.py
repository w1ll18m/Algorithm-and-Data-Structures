from typing import List

class Solution:
    def maximumDetonation(self, bombs: List[List[int]]) -> int:
        def checkInRadius(x, y, a, b, r):
            return ((x - a) ** 2 + (y - b) ** 2) <= r ** 2
        
        # construct the graph -> O(n^2)
        graph = [[] for _ in range(len(bombs))]

        for i in range(len(bombs)):
            for j in range(len(bombs)):
                # check if any other bomb is in range then create a directed edge
                if i != j and checkInRadius(bombs[j][0], bombs[j][1], bombs[i][0], bombs[i][1], bombs[i][2]):
                    graph[i].append(j)

        # count the # of bombs (nodes) that can reached from a given bomb (node)
        def countDetonations(bomb):
            visited = [False for _ in range(len(bombs))]

            def dfs(node):
                if visited[node]: return 0
                visited[node] = True

                count = 1
                # explore the neighbours
                for neighbour in graph[node]:
                    count += dfs(neighbour)
                
                return count
            
            return dfs(bomb)
        
        # determine which bomb (node) will lead to the most detonations (visited nodes) -> O(n^2)
        max_detonation = 0
        for i in range(len(bombs)):
            nofdetonation = countDetonations(i)
            max_detonation = max(max_detonation, nofdetonation)
        
        return max_detonation

    '''
    list of bombs -> bombs[i] = [xi, yi, ri] represents the X-coordinate and Y-coordinate of the ith bomb
                                             with radius ri
    when bomb is detonated -> it detonates neighbouring bombs -> those neighbouring bombs detonate their own neighbours -> GRAPH LIKE BEHAVIOUR (chain of events)

    observe that bomb 1 will only detonate bomb 2 if (x2, y2) is in the area of bomb 1
        - area of bomb 2 COULD OVERLAP with area of bomb 1 BUT (x2, y2) COULD BE OUTSIDE area of bomb 1
        - (x2, y2) COULD BE INSIDE area of bomb 1 while (x1, x2) COULD BE OUTSIDE area of bomb 2 -> need directed edges

    # of bombs that can be detonated -> # of nodes that can be reached -> DFS
    bomb that can denote max -> node that can reach max -> DFS on every single node

    (1) construct the graph and calculate the edges -> O(n^2)
        (a) for each bomb (node), check if any other bombs are in its range
            - check if (x, y) lies in circle by checking if x^2 + y^2 <= r^2
        (b) create a directed edge to any bombs that are in its range
    (2) perform DFS on each bomb (node) and record the bomb that visits the most nodes -> O(n^2)

    thus total time complexity should be O(n^2) and total space complexity of O(n + m) to store graph representation
    '''