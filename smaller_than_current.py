class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        
        Ans=[0]*len(nums)

        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[i] > nums[j]:
                    Ans[i]+=1
        return Ans
