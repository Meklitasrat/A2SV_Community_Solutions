class Solution:
    def largestNumber(self, arr: List[int]) -> str:
        ans = ''
        for i in range(len(arr)):
            arr[i] = str(arr[i])

        for i in range(len(arr)):
            for j in range(i + 1, len(arr)):
                if arr[i] + arr[j] < arr[j] + arr[i]:
                    arr[i], arr[j] = arr[j], arr[i]
        for i in arr:
            ans += i

        return ans if ans[0] != '0' else '0'

# Test the function
