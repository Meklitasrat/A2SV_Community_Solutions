# Enter your code here. Read input from STDIN. Print output to STDOUT
my_set = set()

no_eng = int(input())
eng_sub = [int(x) for x in input().split()]
no_fre = int(input())
fre_sub = [int(x) for x in input().split()]

for i in eng_sub:
    my_set.add(i)
for i in fre_sub:
    my_set.add(i)

print(len(my_set))
