class Solution:
    def interpret(self, comm: str) -> str:
        count = 0
        char  = ''
        
        while count < len(comm):
            if comm[count] == 'G':
                char+='G'
                count +=1
            elif comm[count] == '(' and comm[count +1] ==')':
                char+='o'
                count+=2
            elif comm[count] =='(' and comm[count+1] =='a':
                char+='al'
                count+=4
            else:
                return char
    

        return char
