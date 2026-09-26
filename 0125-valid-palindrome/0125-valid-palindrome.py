class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = []
        for char in s:
            if char.isalnum():
                word.append(char.lower())
        word = "".join(word)
        reverse = word[::-1]
        return word == reverse