class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # Initialize a frequency table for the first word
        freq = [0] * 26
        for char in words[0]:
            freq[ord(char) - ord('a')] += 1

        # Update the frequency table by comparing with the remaining words
        for word in words[1:]:
            curr_freq = [0] * 26
            for char in word:
                curr_freq[ord(char) - ord('a')] += 1
            
            # Update the frequency table by taking the minimum count
            for i in range(26):
                freq[i] = min(freq[i], curr_freq[i])

        # Create the result list based on the frequency table
        result = []
        for i in range(26):
            if freq[i] > 0:
                char = chr(i + ord('a'))
                result.extend([char] * freq[i])

        return result
