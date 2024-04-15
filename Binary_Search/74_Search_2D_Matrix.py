class Solution(object):                                                                # O(log(m) + log(n)) time
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        start = 0
        end = len(matrix) - 1
        rowtosearch = -1

        while start <= end:                                                            # O(log m) time
            middle = (start + end) // 2
            if matrix[middle][0] <= target <= matrix[middle][-1]:
                rowtosearch = middle
                break
            elif matrix[middle][-1] < target:
                start = middle + 1
            else:
                end = middle - 1
        
        if rowtosearch == -1:
            return False
        
        start = 0
        end = len(matrix[rowtosearch]) - 1

        while start <= end:                                                            # O(log n) time
            middle = (start + end) // 2
            if matrix[rowtosearch][middle] == target:
                return True
            elif matrix[rowtosearch][middle] < target:
                start = middle + 1
            else:
                end = middle - 1
        
        return False
    
    '''
    first integer of each row is greater than the last integer of the previous row -> use binary search
        let middle = (start + end) // 2
            if first integer of row <= target <= last integer of row then binary search that row
            elif last integer of that row < target then start = middle + 1
            elif first integer of that row > target then end = middle - 1
    '''
        
        