class Solution:
    def matrixReshape(self, arr: List[List[int]], r: int, c: int) -> List[List[int]]:

        if len(arr)*len(arr[0]) != c*r:
            return arr
        else:



            Ans = [[0 for _ in range(c)] for _ in range(r)]
            
            row , col = 0 ,0

            for i in range(len(arr)):
                for j in range(len(arr[0])):
                    if row < r and col < c:
                            Ans[row][col] = arr[i][j]
                            col+=1
                            
                                
                    if col == c:
                        row+= 1
                        col=0
        
            return Ans
        
        
