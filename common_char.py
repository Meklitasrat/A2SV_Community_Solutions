class Solution(object):
    def commonChars(self, words):
        liss = []
        word_list = list(words[0])
        for w in word_list:
            found = True
            for j in range(1, len(words)):
                if w in words[j]:
                    words[j] = words[j].replace(w, '', 1)  
                else:
                    found = False
                    break
            if found:
                liss.append(w)

        return(liss)
