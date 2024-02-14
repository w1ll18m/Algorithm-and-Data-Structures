class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        scount = {}
        for i in range(len(s)):
            if s[i] not in scount:
                scount[s[i]] = 1
            else:
                scount[s[i]] += 1
        
        tcount = {}
        for i in range(len(t)):
            if t[i] not in tcount:
                tcount[t[i]] = 1
            else:
                tcount[t[i]] += 1
        
        return scount == tcount

    # pattern: two strings are anagrams if they have the same characters -> counting the # of elements (aka characters) -> hashing
