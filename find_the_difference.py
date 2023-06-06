class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_count = [0] * 26  # Array to store the count of each lowercase letter
        
        for char in s:
            char_count[ord(char) - ord('a')] += 1  # Increment count for each character in s
        
        for char in t:
            char_count[ord(char) - ord('a')] -= 1  # Decrement count for each character in t
        
        for i in range(26):
            if char_count[i] == -1:
                return chr(ord('a') + i)  # Return the added letter
