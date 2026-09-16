# array of length 26: index for each letter in the alphabet

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        alph_arr = [0] * 26

        for i in range(len(s)):
            alph_arr[ord(s[i]) - ord('a')] += 1 
            alph_arr[ord(t[i]) - ord('a')] -= 1

        return alph_arr == [0] * 26        