class Solution(object):
    def checkInclusion(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        count = dict()
        for i in range(len(s1)):
            if s1[i] in count:
                count[s1[i]] += 1
            else:
                count[s1[i]] = 1

        curcount = dict(count)
        lofsubstring = 0
        left = 0
        right = left

        while right < len(s2):
            if s2[right] in curcount:
                if curcount[s2[right]] != 0:
                    curcount[s2[right]] -= 1
                    lofsubstring += 1

                else:
                    while s2[left] != s2[right]:                # move left pointer to first instance of the character
                        curcount[s2[left]] += 1                 # update the count as left pointer is being moved
                        lofsubstring -= 1                       # update the lenofsubstring as left pointer is being moved       
                        left += 1
                    left += 1                                   # need to increment left by 1 since we want to move it past the first instance
            
            else:
                curcount = dict(count)                          # reset count
                lofsubstring = 0
                left = right + 1                                # move the left pointer past the character not part of the permutation
            
            if lofsubstring == len(s1):
                return True

            right += 1

        return False


        '''
        permutation is like an anagram -> use hashmaps to count nof characters
        keep left pointer for beginning of substring and right pointer for current position in string 2 -> use sliding window
        both left and right pointers only increment by 1 -> iterate through max 2n characters where n is len(s2) -> O(n) time complexity

        iterate through string 2:
            - if character matches a character in string 1 then subtract count in hashmap
            - if character does not match a character in string 1 then reset count
            - if character matches but count for that character is already 0 then move left pointer past the first instance of that character
                - update the count along the way
            - if length of the substring is the same as the length of string 1 then there is a permutation
        '''
        