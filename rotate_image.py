class Solution:
    def rotate(self, arr: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for i in range(len(arr)):
                p1= 0
                p2= len(arr)-1
                while p1 <p2:
                    arr[p1][i] , arr[p2][i] = arr[p2][i] , arr[p1][i]
                    p1+=1
                    p2 -=1

        for i in range(len(arr)):
            for j in range(i +1, len(arr[0])):
                arr[j][i] , arr[i][j] = arr[i][j], arr[j][i]
                
        
        
