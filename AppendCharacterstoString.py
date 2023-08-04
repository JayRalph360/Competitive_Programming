class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        t_index = 0
        s_length = len(s)
        t_length = len(t)
        
        for i in range(s_length):
            if t_index < t_length and s[i] == t[t_index]:
                t_index += 1
        
        return t_length - t_index
