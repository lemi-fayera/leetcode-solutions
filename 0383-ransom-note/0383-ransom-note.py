class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        ransom_freq = Counter(ransomNote)
        magazine_freq = Counter(magazine)

        for char in ransom_freq:
            if ransom_freq[char] > magazine_freq[char]:
                return False
        return True