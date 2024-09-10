from typing import List

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        valid = []
        phash = {}
        shash = {}

        if len(s) < len(p):
            return []

        # Use hashing to count the number of letters in p
        for char in p:
            if char in phash:
                phash[char] += 1
            else:
                phash[char] = 1
        
        left, right = 0, 0
        while right < len(s):
            # Increment hash table of s if last letter of current window is part of hash table of p
            if s[right] in shash:
                shash[s[right]] += 1
            elif s[right] in phash:
                shash[s[right]] = 1

            # Process the window if it is the same length as p
            if right - left == len(p) - 1:
                # If the hash tables of p and s are the same then it is a valid anagram
                if shash == phash:
                    valid.append(left)
                # Decrement hash table of s if first letter of current window is part of hash table of p
                if s[left] in phash:
                    shash[s[left]] -= 1
                left += 1
            
            right += 1
        
        return valid

    '''
    given strings s and p, find p's anagrams in s
    anagrams -> use hashing to count the number of letters in p
    want to see if any of the subarrays in s form an anagram of p -> sliding window

    maintain a sliding window of size len(p)
    use hashing to count the number of letters in that window
    if the hash table of the window and the hash table of p are equal then it is a valid anagram
        - checking equality is O(1) since there are max 26 keys in the hash table (only 26 letters)
    '''
        