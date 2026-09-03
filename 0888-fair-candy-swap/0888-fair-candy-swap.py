class Solution:
    def fairCandySwap(self, aliceSizes: list[int], bobSizes: list[int]) -> list[int]:
        alice_sum = sum(aliceSizes)
        bob_sum = sum(bobSizes)

        diff = (alice_sum - bob_sum) // 2

        bob_set = set(bobSizes)

        for x in aliceSizes:
            y = x - diff

            if y in bob_set:
                return [x, y]

        return []