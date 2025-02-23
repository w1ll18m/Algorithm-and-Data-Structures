from typing import List

class Solution:
    def minimumHealth(self, damage: List[int], armor: int) -> int:
        # intialize counter variables
        greatest_damage = 0
        total_damage = 0

        # iterate through the array to find sum of elements and max element
        for i in range(len(damage)):
            total_damage += damage[i]
            greatest_damage = max(greatest_damage, damage[i])
        
        # calculate damage shielded using the armor
        protected_damage = min(armor, greatest_damage)
        total_damage -= protected_damage

        return total_damage + 1

    '''
    damage[i] -> represents the amount of health lost to complete the ith level
    armor -> protect you from at most armor damage
    to beat the game, must complete levels in order and your health must be greater than 0 at all times

    we need to travel through all levels -> our health must be at least (sum(damage) + 1)
        - the greedy sol is to find the level with the greatest damage and use the shield there
            - maximizes the amount of damage shielded

    (1) iterate through the array and sum up all the values while keeping track of greatest element
    (2) we protect either min(greatest, armour) damage -> subtract that from result
        - if armour > greatest then we can only protect greatest damage since we can only use shield once (and it doesnt heal)
        - if greatest >= armour then we can only protect armour damage since that is the max we can protect
    (3) add return result + 1

    thus total time complexity is O(n) and total space complexity is O(1)
    '''