class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        
        combinations = []

        def findParanthesis(nofleft, nofright, cur):
            newlofcombos = []

            if nofleft < n and nofright < n:
                possibilities_1 = findParanthesis(nofleft + 1, nofright, cur + "(")
                newlofcombos.extend(possibilities_1)

                if cur != "" and nofright < nofleft:
                    possibilities_2 = findParanthesis(nofleft, nofright + 1, cur + ")")
                    newlofcombos.extend(possibilities_2)
            
            elif nofright < n:
                possibilities = findParanthesis(nofleft, nofright + 1, cur + ")")
                newlofcombos.extend(possibilities)
            
            else:
                return [cur]
            
            return newlofcombos
        
        combinations = findParanthesis(0, 0, "")
        return combinations

        