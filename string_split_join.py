def split_and_join(line):
    # write your code here
    
    lists = line.split(" ")
    
    strs = '-'.join(lists)
    
    return strs
    

if __name__ == '__main__':
    line = input()
    result = split_and_join(line)
    print(result)
