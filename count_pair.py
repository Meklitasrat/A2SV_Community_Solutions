class Solution:
    def similarPairs(self, words: List[str]) -> int:

        count = 0
        Ans = []

        for i in words:
           item = ''.join(set(i))
           Ans.append(item)

        for i in range(len(Ans)):
            Ans[i] = sorted(Ans[i])

        Ans = [''.join(s) for s in Ans]

        for i in range(len(Ans)):
            for j in range(1+i, len(Ans)):
                if Ans[i] == Ans[j]:
                    count+=1

        return count



