class Solution:
    def secondHighest(self, s: str) -> int:
        arr=[]
        for i in s: 
            if i.isdigit():
                arr.append(int(i))
        
        arr1=list(set(arr))
        arr1.sort()

        if len(arr1) >= 2:
            return arr1[-2]
        return -1
        


        