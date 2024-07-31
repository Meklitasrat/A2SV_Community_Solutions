class Solution:
    def maxIceCream(self, arr: List[int], coin: int) -> int:
        sum = 0
        pointer =0
        arr = sorted(arr)

        if arr[0] > coin:
            return 0

        else:
            while sum < coin and pointer <len(arr):
                sum+=arr[pointer]
                if sum <= coin:
                    pointer+=1
            return pointer
        
