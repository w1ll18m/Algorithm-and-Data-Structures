from typing import List

class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        followers = {}
        following = {}

        # trust[i][0] is a and trust[i][1] is b
        for i in range(len(trust)):
            # update b's followers count
            followers[trust[i][1]] = followers.get(trust[i][1], 0) + 1
            # update a's following count
            following[trust[i][0]] = following.get(trust[i][0], 0) + 1    

        for i in range(1, n + 1):
            # check if town judge
            if followers.get(i, 0) == n - 1 and following.get(i, 0) == 0:
                return i
        
        return -1
    
    '''
    town judge trusts nobody 
    everybody trusts the town judge

    how can we check if everybody trusts the town judge? -> for each person x, maintain a list of people who trust them
                                                            if a person has a list of size n - 1 then everyone but them trusts them
    how can we check who a person trusts? -> for each person x, maintain a list of people that they trust
                                             if a person has a list of size 0 then they trust no one
    sounds like we need two linked lists!!! -> iterate through list once to construct hashmaps -> O(len(trust))
    
    how can we check if somebody is the town judge? -> check if their following list is size 0 and their followers list is size n - 1
    we need to check potentially everyone -> O(n) complexity
    thus total time complexity is O(n +  len(trust)) and O(n) space complexity
    '''