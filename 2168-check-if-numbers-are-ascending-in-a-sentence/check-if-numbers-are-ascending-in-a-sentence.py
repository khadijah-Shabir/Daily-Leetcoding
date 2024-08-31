class Solution:
    def areNumbersAscending(self, s: str) -> bool:
        arr=[]
        res=s.split()
        for i in range(len(res)):
            if res[i].isnumeric():
                arr.append(int(res[i]))

        boolean=True
        for i in range(len(arr)-1):
            if arr[i]>=arr[i+1]:
                boolean=False
                break
        return boolean



              

        
        


        