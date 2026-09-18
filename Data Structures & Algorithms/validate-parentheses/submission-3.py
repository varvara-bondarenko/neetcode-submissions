class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) == 1: 
            return False
            
        valid_pairs = {'}': '{', ')': '(', "]": "["}
        tracker = [] # stack

        for i in range(len(s)):
            if s[i] not in valid_pairs.keys():
                tracker.append(s[i])
                # '[['
            else: 
                if tracker:
                    last_el = tracker.pop()
                    if last_el != valid_pairs[s[i]]:
                        return False
                else: 
                    return False
            
        if tracker: 
            return False
        
        return True