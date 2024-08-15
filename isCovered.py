class Solution:
    def isCovered(self, arr: List[List[int]], left: int, right: int) -> bool:
        Ans = []
        res =[]
        to_be_removed = []
        for i in range(left, right+1):
            Ans.append(i)

        
        for i in arr:
            res.extend(k for k in range(i[0], i[1]+1))

        for i in Ans:
            if i in res:
                to_be_removed.append(i)
        for i in to_be_removed:
            Ans.remove(i)

    
        if Ans:
            return False
        else:
            return True
