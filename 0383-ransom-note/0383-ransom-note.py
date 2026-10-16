class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        rans_freq = Counter(ransomNote)
        mag_freq = Counter(magazine)
        can = True
        for char in ransomNote:
            if char not in magazine:
                return False
            if char in magazine and rans_freq[char] > mag_freq[char]:
                can = False
        return can