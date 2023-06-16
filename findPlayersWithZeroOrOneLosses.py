from typing import List

class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winners = {}
        losers = {}

        for match in matches:
            winner, loser = match[0], match[1]
            winners[winner] = winners.get(winner, 0) + 1
            losers[loser] = losers.get(loser, 0) + 1

        not_lost = [player for player in winners if player not in losers]
        lost_once = [player for player in losers if losers[player] == 1]

        return [sorted(not_lost), sorted(lost_once)]
