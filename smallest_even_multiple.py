class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        def gcd(a: int, b: int) -> int:
            while b:
                a, b = b, a % b
            return a

        return n // gcd(n, 2) * 2
