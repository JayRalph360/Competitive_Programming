class Solution:
    def percentageLetter(self, s: str, letter: str) -> int:
        count = 0
        for c in s:
            if c == letter:
                count += 1
        return int(count / len(s) * 100)
