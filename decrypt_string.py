class Solution:
    def freqAlphabets(self, s: str) -> str:
        result = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i + 2] == '#':
                # Handle mapping for two-digit characters
                num = int(s[i:i + 2])
                result += chr(ord('j') + num - 10)
                i += 3
            else:
                # Handle mapping for single-digit characters
                num = int(s[i])
                result += chr(ord('a') + num - 1)
                i += 1
        return result
