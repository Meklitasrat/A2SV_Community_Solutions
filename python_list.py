if __name__ == '__main__':
    N = int(input())
    
    listt = []
    
    for i in range(N):
        new_lis = input().split()
        command = new_lis[0]
        
        if command == 'insert':
            index = int(new_lis[1])
            value = int(new_lis[2])
            listt.insert(index, value)
        elif command == 'append':
            value = int(new_lis[1])
            listt.append(value)
        elif command == 'print':
            print(listt)
        elif command == 'sort':
            listt.sort()
        elif command == 'pop':
            listt.pop()
        elif command == 'reverse':
            listt.reverse()
        elif command == 'remove':
            listt.remove(int(new_lis[1]))
