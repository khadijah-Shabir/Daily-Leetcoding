class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count=0
        for i in range((len(words))):
            temp=0
            for j in range(len(words[i])):
                if words[i][j] in allowed:
                    temp+=1
            if len(words[i])==temp:
                count+=1
        return count

                




        