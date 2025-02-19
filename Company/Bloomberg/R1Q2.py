'''
Wordle

word_bank = [...]
target = LAYER

TABLE
-*-++

XYYYY
-+*--

LAYER

L -> 1
A -> 1
Y -> 1
E -> 1
R -> 

validate -> 1 iteration 
*****

'''

from collections import defaultdict

class Word_Bank:
    def __init__(self, words):
        nofwords = len(words) - 1
        idx = rand(0, nofwords)
        
        self.target = words[idx]
        
        self.word_count = defaultdict(int)
        for char in self.target:
            self.word_count[char] += 1
    
    def validate(guess: str) -> str:
        results = ""
        for i in range(len(guess)):
            results += "-"
        
        word_count = shallow_copy(self.word_count)
        
        for i in range(len(guess)):
            if guess[i] == self.target[i]:
                word_count[guess[i]] -= 1
                results[i] = "*"
            
        for i in range(len(guess)):
            if word_count[guess[i]] > 0:
                word_count[guess[i]] -= 1
                results[i] = "+"
        
        return results