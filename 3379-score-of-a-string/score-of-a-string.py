class Solution:
    def scoreOfString(self, s: str) -> int:
        arr = []
        for i in range(len(s)-1):
            arr.append( abs ((ord(s[i]))  - ord(s[i+1]))  )

        addition = sum(arr)

        return addition