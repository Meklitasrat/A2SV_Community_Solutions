class Solution:
    def smallestNumber(self, num: int) -> int:

        if num== 0:
            return 0
        if num>0:

            zero_count=0
            
            my_num= str(num)
            small= min(my_num)
            if small== "0":
                for i in my_num:
                    if i =="0":
                        my_num = my_num.replace(small,"",1)
                        zero_count+=1
            real_small= min(my_num)
            my_num= list(my_num)
            my_num.remove(real_small)
            my_num.insert(0, real_small)
            my_num+=["0"]*zero_count
            my_num[1:len(my_num)]= sorted(my_num[1:len(my_num)])
            my_num=''.join(my_num)
            return int(my_num)
        else:
            num= str(num)
            num= list(num)
            num.remove("-")
            num= sorted(num,reverse=True)
            num=''.join(num)
            num= -abs(int(num))
            return num
