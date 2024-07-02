class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        Ans = [[] for _ in range(len(matrix[0]))]

        for i in range (len(matrix[0])):
                for j in range(len(matrix)):
                    Ans[i].append(matrix[j][i])
  
        return Ans

