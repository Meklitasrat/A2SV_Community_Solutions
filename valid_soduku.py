class Solution:
    def isValidSudoku(self, arr: List[List[str]]) -> bool:
        def check_whole(arr):

            for i in range(9):
                x=[]
                for j in range(9):
                    if arr[j][i] =='.':
                        continue
                    else:
                        x.append(arr[j][i])
                if len(set(x)) == len(x):
                    continue
                else:
                    return False
                    
                
                
            for i in range(9):
                x=[]
                for j in range(9):
                    if arr[i][j] =='.':
                        continue
                    else:
                        x.append(arr[i][j])
                if len(set(x)) == len(x):
                    continue
                else:
                    return False
            return True
                
        def check_windows(board):
            for n in range(0, 9, 3): 
                for m in range(0, 9, 3): 
                    seen = set()
                    for i in range(3):
                        for j in range(3):
                            num = board[n + i][m + j]
                            if num != '.':
                                if num in seen:
                                    print(False)
                                    return
                                seen.add(num)
            return True

        return check_whole(arr) and check_windows(arr)
        
