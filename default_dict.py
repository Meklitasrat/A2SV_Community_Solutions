n, m = map(int, input().split())
a = []
for _ in range(n):
    a.append(input())
b = []
for _ in range(m):
    b.append(input())


ans = []

for word in b:
    indices = []
    for i, w in enumerate(a):
        if w == word:
            indices.append(i+1)
    if indices:
        print(" ".join(map(str, indices)))
    else:
        print(-1)


