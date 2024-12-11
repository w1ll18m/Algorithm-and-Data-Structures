from typing import List

class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        # sort the array
        tokens.sort()

        current_score = 0
        i, j = 0, len(tokens) - 1
        while i < j:
            # take the smallest token if we have enough power
            if power >= tokens[i]:
                power -= tokens[i]
                current_score += 1
                i += 1
            # take the largest token for more power if we have enough score
            elif current_score > 0:
                power += tokens[j]
                current_score -= 1
                j -= 1
            # no more moves can be made if we don't have enough power or score
            else:
                break
        
        # take the last token if we have enough power
        if i == j and power >= tokens[i]:
            power -= tokens[i]
            current_score += 1
        
        return current_score

    '''
    tokens is an integer array -> tokens[i] represents the value of token i
    start with specified power and initial score of 0
    maximize the total score which is calculated as followed:
        - during each turn, choose an unplayed token
        (i) play token face-up
            - current power must be at least tokens[i]
            - lose tokens[i] power and gain 1 score
        (ii) play token face-down
            - current score is at least 1
            - gain tokens[i] power and lose 1 score
    
    maximize score -> dp? -> no since we can play tokens in any order (no recursive subproblems)
        - ex) lets say we play token 1 first then subproblem becomes either 
              (1) power + tokens[1], tokens 2 to n
              (2) power - tokens[1], tokens 2 to n
        - in the first scenario, power increases so we don't have a smaller subproblem

    integer array -> sort the array? -> greedy solution where we want to taken the smallest tokens first?
    (1) sort the array

    (2) maintain 2 pointers i and j that point to the smallest and largest tokens respectively

    (3) while i < j:
        (i) want to take smallest available token first -> take tokens[i] if power >= tokens[i]
        (ii) if not enough power then take largest available token for power -> take tokens[j] if power < tokens[j] 
            - tokens[j] > tokens[i] since array is sorted so we will have enough power to take tokens[i] next turn

    (4) if i == j after the while loop:
        (i) take the token if power >= tokens[i]
        (ii) do not take the token if power < tokens[i]
    
    thus total time complexity is O(nlogn) for sorting and total space complexity is O(1)
    '''