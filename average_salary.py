class Solution:
    def average(self, salary: List[int]) -> float:
        total = sum(salary) - min(salary) - max(salary)
        count = len(salary) - 2
        return total / count
