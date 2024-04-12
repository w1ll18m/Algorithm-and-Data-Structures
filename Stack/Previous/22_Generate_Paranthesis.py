class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        if n == 1:
            return ["()"]
        
        combinations = self.generateParenthesis(n - 1)
        new_combinations = []
        for i in range(len(combinations)):
            addleft = "()" + combinations[i]
            addright = combinations[i] + "()"
            
            new_combinations.append(addleft)
            if addleft != addright:
                new_combinations.append(addright)
            
            new_combinations.append("(" + combinations[i] + ")")

        return new_combinations
        