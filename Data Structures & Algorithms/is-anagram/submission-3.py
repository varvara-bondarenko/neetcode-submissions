class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if hash(str(sorted(s))) == hash(str(sorted(t))):
            return True 
        
        return False
        