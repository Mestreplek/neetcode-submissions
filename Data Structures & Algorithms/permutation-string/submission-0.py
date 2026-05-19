def count_dict(s1: str):
    s1_count = {}
    for c in s1:
        if c in s1_count:
            s1_count[c] += 1
        else:
            s1_count[c] = 1
    return s1_count

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        s1_count = count_dict(s1)
        s1_length = len(s1)
        window_count = count_dict(s2[0:s1_length])
        

        if window_count == s1_count:
            print("first true")
            return True 
        
        for i in range(1,len(s2) - len(s1) + 1):
            old_c = s2[i-1]
            if window_count[old_c] == 1:
                window_count.pop(old_c)
            else:
                window_count[old_c] -= 1 


            new_c = s2[i+s1_length-1]
            if new_c in window_count:
                window_count[new_c] += 1
            else:
                window_count[new_c] = 1
            if window_count == s1_count:
                return True
        return False


             

