from collections import defaultdict 

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t: 
            return True 

        if len(s) != len(t):
            return False

        count_dict_s = {}
        count_dict_t = {}

        for i in range(len(s)):
            if s[i] in count_dict_s: 
                count_dict_s[s[i]] += 1 
            else: 
                count_dict_s[s[i]] = 1

            if t[i] in count_dict_t: 
                count_dict_t[t[i]] += 1 
            else: 
                count_dict_t[t[i]] = 1

        for key, value in count_dict_s.items(): 
            if key not in count_dict_t: 
                return False
            
            if value != count_dict_t[key]:
                return False

        return True
