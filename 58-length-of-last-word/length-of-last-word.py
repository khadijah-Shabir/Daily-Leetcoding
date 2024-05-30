class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        # Trim leading and trailing white spaces
        s = s.strip()
        
        # Split the string by spaces
        words = s.split()
        
        # If the resulting list is empty, return 0
        if not words:
            return 0
        
        # Return the length of the last word
        return len(words[-1])
        