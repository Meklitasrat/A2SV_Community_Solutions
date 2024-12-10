class Solution:
    def maxCoins(self, arr: List[int]) -> int:

        arr = sorted(arr)
        num = len(arr)
        Ans =0 
        temp_arr = arr[:]

        for i in range(num//3):
            print(Ans)

            x = len(temp_arr) -1
            Ans+=temp_arr[x-1]
            temp_arr.pop(x)
            temp_arr.pop(0)

            x = len(temp_arr) - 1  
            if x >= 0:  
                temp_arr.pop(x - 1)
        
        return Ans
