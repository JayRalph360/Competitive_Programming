class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        s = 0
        i = 0
        while tickets[k] != 0:
            if tickets[i] != 0:
                tickets[i] -= 1
                s += 1
            i = (i+1) % len(tickets)
        return s
