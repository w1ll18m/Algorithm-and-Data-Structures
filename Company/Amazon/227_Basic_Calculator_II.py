class Solution:
    def calculate(self, s: str) -> int:
        ops = set(['+', '-', '*', '/'])
        exp_stack_1 = []
        exp_stack_2 = []
        s = s.replace(' ', '')

        # push the first integer of the expression onto the stack
        exp_stack_1.append(int(s[0]))

        # process the rest of the expression (pass 1)
        for i in range(1, len(s)):
            # push operators onto the stack
            if s[i] in ops:
                exp_stack_1.append(s[i])
                continue
            
            # convert the character to an integer
            b = int(s[i])

            # check if top of the stack is another integer
            if exp_stack_1[-1] not in ops:
                a = exp_stack_1.pop()
                b = a * 10 + b
            
            # push the next integer onto the stack
            exp_stack_1.append(b)

        # reverse the first pass stack so that we process the expression in the correct order
        exp_stack_1.reverse()
        # print(exp_stack_1)
        # push the first integer of the expression onto the second pass stack
        exp_stack_2.append(exp_stack_1.pop())
        
        # process the multi-digit expression (pass 2)
        while len(exp_stack_1) > 0:
            # push operators onto the second pass stack
            if exp_stack_1[-1] in ops:
                op = exp_stack_1.pop()
                exp_stack_2.append(op)

            # pop the integer from the first pass stack
            b = exp_stack_1.pop()

            # check if top of the second pass stack is "*" or "/"
            if exp_stack_2[-1] == '*' or exp_stack_2[-1] == '/':
                # pop the previous integer from the stack
                op = exp_stack_2.pop()
                a = exp_stack_2.pop()
                # perform the corresponding operation
                if op == '*':
                    b = a * b
                elif op == '/':
                    b = a // b
            
            # push the next integer onto the second pass stack
            exp_stack_2.append(b)
        
        # reverse the second pass stack so that we process the expression in the correct order
        exp_stack_2.reverse()
        # print(exp_stack_2)

        # the expression stack represents an equation with only addition/subtraction -> pop all elements
        op = '+'
        result = 0
        while len(exp_stack_2) > 0:
            if exp_stack_2[-1] == '+' or exp_stack_2[-1] == '-':
                op = exp_stack_2.pop()
            else:
                b = exp_stack_2.pop()
                if op == '+':
                    result = result + b
                elif op == '-':
                    result = result - b
        
        return result

    '''
    s -> represents an expression
        - evaluate this expression and return its value
        - integer division should truncate toward zero (use floor)

    3 + 2 * 2 -> 7
    3 / 2 -> 1
    3 + 5 / 2 -> 5

    we want to evaluate '*' and '/' operations first!!!
    pass through the string thrice? -> O(n)
        - evaluate all multi-digit integers in the first pass
        - evaluate all "*" and "/" operations in the second pass
        - evaluate all "+" and "/" operations in the third pass

    let's push each character (int and op) onto a stack in the first pass!!!
        - if current character represents an integer and the top of the stack is also an integer (handle multi-digit numbers)
            - pop item from the stack -> a = pop()
            - calculate a * 10 + cur_char and push that onto the stack
        - otherwise push the character onto the stack
    
    we can repeat with the "*" and "/" operations in the second pass
        - if current character represents an integer and the top of the stack is "*" or "/"
            - pop two items from the stack -> op = pop() and a = pop()
            - calculate a / cur_char and push that onto the stack
        - otherwise push the character onto the stack
    
    once we do this for "*" and "/" operations in the second pass then we repeat with "+" and "-" operations in the third pass

    thus total time complexity is O(n) for 3 passes through the array and total space complexity is O(n) for the stack

    NOTE: USE STACK FOR EVALUATING EXPRESSIONS!!!
    '''