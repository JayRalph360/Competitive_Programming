from typing import List

class TopVotedCandidate:

    def __init__(self, persons: List[int], times: List[int]):
        self.times = times
        self.leaders = []
        leader_count = {}
        current_leader = None  # Initialize to None
        
        for i in range(len(persons)):
            person = persons[i]
            time = times[i]
            
            if person not in leader_count:
                leader_count[person] = 0
            leader_count[person] += 1
            
            if current_leader is None or leader_count[person] >= leader_count[current_leader]:
                current_leader = person
            
            self.leaders.append(current_leader)

    def q(self, t: int) -> int:
        l, r = 0, len(self.times) - 1
        
        while l < r:
            mid = (l + r + 1) // 2
            if self.times[mid] <= t:
                l = mid
            else:
                r = mid - 1
        
        return self.leaders[l]
