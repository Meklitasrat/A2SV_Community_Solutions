def d_x_sum(arr):

    max_num =0


    for i in range(len(arr)):
        for j in range(len(arr[0])):

            lr = 0
            row , col = i , j
            while 0 <= row < len(arr) and 0 <= col < len(arr[i]):
                lr += arr[row][col]
                row+=1
                col+=1

            rl=0
            row , col = i , j
            while 0 <= row < len(arr) and len(arr[i]) > col >= 0:
                rl+=arr[row][col]
                row+=1
                col-=1
            btr =0
            row , col = i , j
            while row >= 0 and col < len(arr[i]):
                btr+= arr[row][col]
                row-=1
                col+=1
            
            btl=0
            row , col = i , j
            while row >= 0 and len(arr[i])> col >= 0:
                btl+= arr[row][col]
                col-=1
                row-=1

           

            sum = (rl +lr +btl +btr) - 3*arr[i][j]

            max_num = max(max_num , sum)

    print(max_num)


d_x_sum([[1 ,2 ,2, 1] ,[2 ,4 ,2 ,4], [2, 2 ,3 ,1], [2, 4 ,2 ,4]])
