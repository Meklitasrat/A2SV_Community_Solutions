sup = list(input().split())
n = int(input())

Ans = []
for i in range(n):
    sub = list(input().split())
    
    if len(sup) <= len(sub):
        Ans.append('False')
        break
    else:
        for j in sub:
            if j not in sup:
                Ans.append('False')
                break
        else: 
            Ans.append('True')
            
if 'False' in Ans:
    print(False)
else:
    print(True)
