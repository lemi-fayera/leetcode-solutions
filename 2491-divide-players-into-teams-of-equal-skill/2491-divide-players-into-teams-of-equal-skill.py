class Solution:
    def dividePlayers(self, skill: list[int]) -> int:
        sorted_skill = skill.sort()
        left = 0
        right = len(skill)-1
        total = []
        product = []
        while left < right:
            total.append(skill[right] + skill[left])
            product.append(skill[right] * skill[left])
            left += 1
            right -= 1
        if len(set(total)) == 1:
            return sum(product)
        else:
            return -1