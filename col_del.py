class Solution:
    def minDeletionSize(self, str: List[str]) -> int:
        count  = 0

        for col in range(len(str[0])):
            for row in range(1 , len(str)):
                if str[row][col] < str[row -1][col]:
                    count +=1
                    break

        return count
