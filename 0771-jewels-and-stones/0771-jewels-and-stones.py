class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        jew = []
        for stone in stones:
            if stone in jewels:
                jew.append(stone)
        return len(jew)