class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_freq = Counter(ransomNote)
        mag_freq = Counter(magazine)

        for char in rans_freq:
            if rans_freq[char] > mag_freq[char]:
                return False
        return True