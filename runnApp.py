if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    Arr = []
    for i in arr:
        Arr.append(i)
    nn = max(n for n in Arr)
    Arr.remove(nn)
    nn = max(n for n in Arr)
    Arr.remove(nn)

    
    Ans = max(n for n in Arr)
    
    print(Ans)
