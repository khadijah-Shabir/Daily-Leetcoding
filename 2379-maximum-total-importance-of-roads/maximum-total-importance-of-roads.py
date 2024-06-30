class Solution:
    def maximumImportance(self, n: int, roads: List[List[int]]) -> int:
        arr=[0]*n
        for i, j in roads:
            arr[i]+=1
            arr[j]+=1

        arr.sort()
        point=1
        res=0
        for i in arr:
            res+=i*point
            point+=1
        return res


      
        