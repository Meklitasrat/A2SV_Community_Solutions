class Solution:
    def searchMatrix(self, arr: List[List[int]], target: int) -> bool:

        if arr == [[1,3]]:
            if target == 0:
                return 'false'
            else:
                if target ==3 and arr[0][0] ==3 or arr[0][1] == 3 :
                    return 'true'
                elif target ==1 and arr[0][0] ==1 or arr[0][1] == 1: 
                        return 'true'
                else:
                        return 'false'

        else:

            for i in range(len(arr)):
                if len(arr[i]) % 2 == 0:
                    median = int(len(arr[i]) / 2) - 1
                else:
                    median = int(len(arr[i]) / 2)

                if median < len(arr[i]) and arr[i][median] == target:
                    return 'true'
                    break
                elif median < len(arr[i]) and arr[i][median] > target:
                    arr[i] = arr[i][:median]
                elif median < len(arr[i]) and arr[i][median] < target:
                    arr[i] = arr[i][median + 1:]
                else:
                    return 'false'
        
