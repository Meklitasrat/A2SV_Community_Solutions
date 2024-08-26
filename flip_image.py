class Solution:
    def flipAndInvertImage(self, arr: List[List[int]]) -> List[List[int]]:
        
        for i in range(len(arr)):
            arr[i] = arr[i][::-1]

        for row in range(len(arr)):
            for col in range(len(arr[0])):
                if arr[row][col] == 1:
                    arr[row][col] = 0
                else:
                    arr[row][col] = 1
        return arr
