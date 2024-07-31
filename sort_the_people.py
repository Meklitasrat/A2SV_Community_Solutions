class Solution:
    def sortPeople(self, name: List[str], arr: List[int]) -> List[str]:

        for i in range(len(arr)):
            for j in range(1+i, len(arr)):
                if arr[i] < arr[j]:
                    arr[i] , arr[j] = arr[j] , arr[i]
                    name[i] , name[j] = name[j] , name[i]

        # bubble sort 

        size = len(arr)

        for i in range(size):
            for j in range(size-i-1):
                if arr[j] < arr[j+1]:
                    arr[j] , arr[j+1] = arr[j+1] , arr[j]
                    name[j] , name[j+1] = name[j+1] , name[j]
                else:
                    continue

        # selectin sort

        for i in range(size):
            for j in range(1+i,size):
                if arr[i] < arr[j]:
                    arr[i] , arr[j] = arr[j] , arr[i]
                    name[i] , name[j] = name[j], name[i]
            
        
        return name
