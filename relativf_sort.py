class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:

        arrr1 = []
        arrr2 = []
        for i in arr1:
            if i in arr2:
                arrr1.append(i)
            else:
                arrr2.append(i)


        def custom_comp(item):
            return arr2.index(item)
        
        arrr1.sort(key = custom_comp)

        arrr2= sorted(arrr2)

        arrr1 = arrr1 + arrr2
        
        return arrr1
        
