from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        values = {}

        counter = 0
        # assign new ASCII values to each letter
        for char in order:
            values[char] = counter
            counter += 1
        
        # O(20) since 1 <= words[i].length <= 20
        def checkIfSmaller(string1: str, string2: str):
            i = 0
            while i < len(string1) and i < len(string2):
                # get the new ASCII values of each character
                value1 = values[string1[i]]
                value2 = values[string2[i]]
                i += 1

                # case 1: characters are the same
                if value1 == value2:
                    continue
                # case 2: string 1 has smaller character than string 2
                elif value1 < value2:
                    return True
                # case 3: string 2 has smaller character than string 1
                else:
                    return False
            
            # case 4: all characters match but string 1 is longer than string 2
            if len(string2) < len(string1):
                return False
            # case 5: all characters match but string 1 is shorter than string 2
            return True

        for i in range(1, len(words)):
            if not checkIfSmaller(words[i-1], words[i]):
                return False
        return True
    
    '''
    how are words typically compared? -> (1) each letter is assigned an ASCII value
                                         (2) letters with lower ASCII values are considered lexographically smaller
                                         (3) to compare strings, iterate through both strings and compare ASCII values of characters
    lets assign new ASCII values to each letter -> ex) hlabcdefgijkmnopqrstuvwxyz then h = 0
                                                                                       l = 1
                                                                                       a = 2
    how can we check the ASCII values of a letter quickly -> map letter to value

    O(26) to iterate through order and construct hashmap
    O(20) to compare two words to see which one is lexographically smaller
    O(n) to iterate through all the words in the list
    thus total time complexity of O(n) and space complexity of O(n)
    '''
