class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        pstack = []
        
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                pstack.append(s[i])

            else:
                if len(pstack) != 0:
                    popped = pstack.pop()
                else:
                    return False

                if (s[i] == ")" and popped != "(") or (s[i] == "}" and popped != "{") or (s[i] == "]" and popped != "["):
                    return False

        if len(pstack) != 0:
            return False
        else:
            return True

        '''
        pattern: paranthesis are nested and need to keep track of order of paranthesis -> use stack

        iterate through the string s:
        - use a stack to keep track of "(", "{", and "]"
        - pop off of stack when we see ")", "{", and "]"
            - if popped character is same type as closing bracket then continue
            - else return false 
        - if we reach end of the string and stack is not empty then return false else return true
        '''