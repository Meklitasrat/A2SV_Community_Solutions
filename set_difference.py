Ans = []

num_eng = int(input())
eng = [int(x) for x in input().split()]
num_fre = int(input())
fre = [int(x) for x in input().split()]

for i in eng:
    if i in fre:
        Ans.append(i)

print(len(Ans))
