class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False
        characters_s = {}
        characters_t = {}

        for char_s in s:
            characters_s[char_s] = characters_s.get(char_s,0) + 1

        for char_t in t:
            characters_t[char_t] = characters_t.get(char_t,0) + 1

        for c, val in characters_s.items():
            if val != characters_t.get(c,0):
                return False

        return True

        
