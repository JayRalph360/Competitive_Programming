class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        current = shifts[-1]
        shifts[-1] = chr((ord(s[-1])-97 + current) % 26 + 97)

        for i in range(len(shifts)-2, -1, -1):
            current += shifts[i]
            shifts[i] = chr((ord(s[i])-97 + current) % 26 + 97)
        return "".join(shifts)
