class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:

        max = 0

        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if max < arr[j]:
                    max = arr[j]   
            

            arr[i] = max
            max = 0

        arr[len(arr) -1] = -1

        return arr
        
