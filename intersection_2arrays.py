class Solution:
    def intersect(self, arr1: List[int], arr2: List[int]) -> List[int]:
        
        ans= []

        c1= Counter(arr1)
        c2= Counter(arr2)

        for k1, v1 in c1.items():
            for k2, v2 in c2.items():
                if k1==k2 and v1!=0 and v2!=0:
                    ans+=[k2]*min(v1,v2)
                                                          
        return ans
