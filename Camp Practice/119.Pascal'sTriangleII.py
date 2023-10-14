class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        currRow = [1] * (rowIndex + 1)
        if rowIndex == 0:
            return currRow
        prevRow = self.getRow(rowIndex - 1)
        for i in range(1, len(currRow)-1):
            print(prevRow[i])
            currRow[i] = prevRow[i-1] + prevRow[i]
        return currRow
