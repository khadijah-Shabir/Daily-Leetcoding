class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        def split(input_string, separator):
            split_substrings = []
            word = ""

            for character in input_string:
                if character != separator:
                    word += character
                else:
                    split_substrings.append(word)
                    word = ""

            if word:
                split_substrings.append(word)

            return split_substrings

        words = split(s, ' ')
        if len(pattern) != len(words):
            return False

        charToWord = {}
        wordToChar = {}

        for char, word in zip(pattern, words):
            if char in charToWord and charToWord[char] != word:
                return False
            if word in wordToChar and wordToChar[word] != char:
                return False
            charToWord[char] = word
            wordToChar[word] = char

        return True