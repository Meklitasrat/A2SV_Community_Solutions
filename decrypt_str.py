class Solution:
    def freqAlphabets(self, s: str) -> str:
    
        start_char = 'a'
        start_num = 1
        map = {}

        for i in range(26):
            if i < 9:
                char = chr(ord(start_char) + i)
                num = str(start_num +i)
                map[num] = char
            
            else:
                char = chr(ord(start_char) +i) 
                num = str(start_num + i ) + '#'
                map[num] = char
        
        count = len(s) -1

        char = ''
        Ans= ''
        
        while count >= 0:
            if s[count] != '#':
                Ans += str(map[s[count]])
                count -=1
            else:
                char+= s[count-2] + s[count-1] + s[count]
                Ans+= str(map[char])
                count -=3
                char =''

        Ans = Ans[::-1]

        return Ans
