class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        max_profit = 0
        current_largest = 0
        left = 0
        right = left + 1

        while right < len(prices):
            if right == len(prices) - 1:                                            # edge case where max_profit subarray/window is at end of the array
                current_largest = max(current_largest, prices[right])
                
                current_profit = current_largest - prices[left]
                max_profit = max(max_profit, current_profit)

            if prices[right] < prices[left]:                                        # case where value of right pointer is less than left pointer
                current_profit = current_largest - prices[left]
                max_profit = max(max_profit, current_profit)

                current_largest = 0
                left = right
            
            elif prices[right] > current_largest:                                   # case where value of right pointer is greater than the largest value seen thus far
                current_largest = prices[right]

            right += 1
        
        return max_profit
        
        '''
        find the window such that the last element minus the first element gives the greatest value
        condition to stop expanding the window: see a value less than the left pointer
        while expanding: keep track of the largest value seen thus far
        processing the window: subtracting the largest value seen thus far and value of left pointer
        '''