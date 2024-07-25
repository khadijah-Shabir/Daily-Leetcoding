class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        array=[]
        spaces_left=0
        for i in range(len(s)): 
            if spaces_left<len(spaces) and i==spaces[spaces_left]: 
                array.append(" ")
                spaces_left += 1
            array.append(s[i])
        return "".join(array)

        