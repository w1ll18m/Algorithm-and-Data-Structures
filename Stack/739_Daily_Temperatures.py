class Solution(object):
    def dailyTemperatures(self, temperatures):
        """
        :type temperatures: List[int]
        :rtype: List[int]
        """

        answer = [None] * len(temperatures)
        notresolved = []

        for i in range(len(temperatures)):
            while len(notresolved) != 0:
                if temperatures[i] <= temperatures[notresolved[-1]]:
                    break
                top = notresolved.pop()
                answer[top] = i - top
                
            notresolved.append(i)
        
        while len(notresolved) != 0:
            answer[notresolved.pop()] = 0
        
        return answer
            
        '''
        keep track of stack of elements whose next greatest element has not been resolved yet
        iterate through the array then for each current element:
        - if the current element is greater than the top of the stack then pop and record answer
        - if the current element is less then add current element to the stack
        - if the stack is empty then add current element to the stack
        note that all elements in the stack are less than the elements below it since an element is only added to the stack if it is less than the top
        '''
        