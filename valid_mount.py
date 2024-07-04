class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        max_num = max(arr)
        index_num= arr.index(max_num)

        if len(arr) < 3 or index_num ==0 or index_num ==len(arr) -1:
            return 'false'
        for i in range(index_num):
            if arr[i] < arr[i+1]:
                continue
            else:
                return'false'

        for i in range(index_num, len(arr)-1):
            if arr[i]> arr[i+1]:
                continue
            else:
                return 'false'

        return 'true'
        
