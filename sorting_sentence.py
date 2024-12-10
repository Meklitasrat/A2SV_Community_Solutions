class Solution:
    def sortSentence(self, s: str) -> str:
        s= s.split(' ')
        Ans= [0]*len(s)

        for i in s:
            x= int(i[len(i)-1])-1
            i= i.replace(i[len(i)-1], "",1)
            Ans[x] = i

        Ans= " ".join(Ans)
        return Ans
        
