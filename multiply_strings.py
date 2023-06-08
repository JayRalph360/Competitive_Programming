class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        m, n = len(num1), len(num2)
        result = [0] * (m + n)

        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                digit1 = int(num1[i])
                digit2 = int(num2[j])
                prod = digit1 * digit2

                # Update the corresponding positions in the result array
                pos1 = i + j
                pos2 = i + j + 1
                sum_val = prod + result[pos2]

                result[pos2] = sum_val % 10
                result[pos1] += sum_val // 10

        # Remove leading zeros from the result
        idx = 0
        while idx < len(result) and result[idx] == 0:
            idx += 1

        if idx == len(result):
            return "0"
        else:
            return "".join(str(digit) for digit in result[idx:])
