class Solution:
    def largestLocal(self, mat: List[List[int]]) -> List[List[int]]:

        Ans = [[] for _ in range(len(mat[0]) -2)]

        for i in range(len(mat)-2):
          for j in range(len(mat[0]) -2):
            
             Ans[i].append(max(mat[i][j] ,mat[i][j+1] , mat[i][j+2], mat[i+1][j] , mat[i+1][j+1] , mat[i+1][j+2] , mat[i+2][j], mat[i+2][j+1] , mat[i+2][j+2]))

            

        return Ans
        
