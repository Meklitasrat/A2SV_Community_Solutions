class Solution:
    def applyOperations(self, s: List[int]) -> List[int]:

       
        i =0
        j =1

        if len(s) == 2 and s[i] == 0 and s[j] !=0 :
            s[0] , s[1] = s[1] , s[0]
            

        while j < len(s) :
        
            if s[i] == s[j]:
                s[i] = s[i]*2
                s[j] = 0

                i+=1
                j+=1
            else:
                i+=1
                j+=1

        
        i = 0
        j = 0

        while j < len(s) -1:
            for k in range(len(s)):
                if s[i] == 0 and s[j] !=0:
                    s[i] , s[j] = s[j] , s[i]
                    i +=1
                    j +=1
                elif s[i] == 0 and s[j] == 0:
                    j+=1

                elif s[i] != 0 and s[j] !=0:
                    i+=1
                    j+=1

        return s
