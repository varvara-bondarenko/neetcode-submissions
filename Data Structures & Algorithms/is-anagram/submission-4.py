from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t: 
            return True 

        if len(s) != len(t):
            return False

        count_dict_s, count_dict_t = {}, {}

        for i in range(len(s)):
            count_dict_s[s[i]] = 1 + count_dict_s.get(s[i], 0)
            count_dict_t[t[i]] = 1 + count_dict_t.get(t[i], 0)

        return count_dict_s == count_dict_t
