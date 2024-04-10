class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """

        token_stack = []

        for i in range(len(tokens)):
            if tokens[i] == "+":
                val1 = token_stack.pop()
                val2 = token_stack.pop()
                token_stack.append(val2 + val1)

            elif tokens[i] == "-":
                val1 = token_stack.pop()
                val2 = token_stack.pop()
                token_stack.append(val2 - val1)

            elif tokens[i] == "*":
                val1 = token_stack.pop()
                val2 = token_stack.pop()
                token_stack.append(val2 * val1)

            elif tokens[i] == "/":
                val1 = token_stack.pop()
                val2 = token_stack.pop()
                token_stack.append(int(float(val2) / val1))

            else:
                token_stack.append(int(tokens[i]))
                
        return token_stack.pop()
        