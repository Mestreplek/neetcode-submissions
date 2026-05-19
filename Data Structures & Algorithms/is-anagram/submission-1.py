class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t): 
            return False 
        for character in s: 
            s_count = s.count(character) 
            t_count = t.count(character) 
            if t_count != s_count: 
                return False 
        return True 