class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        i = 0
        j = len(height) - 1
        maxvolume = (j - i) * min(height[i], height[j])

        while i < j:
            if height[i] < height[j]:
                i += 1
            else:
                j -= 1
            
            if i == j:
                break

            volume = (j - i) * min(height[i], height[j]) 
            maxvolume = max(maxvolume, volume)

        return maxvolume
        
        """
        maintain 2 pointers -> i = 0 and j = len
        volume = min(height[i], height[j]) * width
        increment i or decrement j?
            - width is always decreasing thus only increase in volume can come from increase in min(height[i], height[j])
            - move the pointer with the smallest height
            - moving the pointer with the larger height will always result in a smaller width
                - suppose that height[j] > height[i] 
                    if height[j*] > height[j] then min(height[i], height[j*]) = height[i]
                    if height[i] < height[j*] < height[j] then min(height[i], height[j*]) = height[i]
                    if height[j*] < height[i] < height[j] then min(height[i], height[j*]) = height[j*] < height[i]
        """
