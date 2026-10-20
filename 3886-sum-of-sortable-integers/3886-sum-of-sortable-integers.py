class Solution:
    def sortableIntegers(self, nums):
        n = len(nums)
        target = sorted(nums)
        ans = 0

        # Only consider divisors of n
        divisors = []
        for k in range(1, int(n ** 0.5) + 1):
            if n % k == 0:
                divisors.append(k)
                if k != n // k:
                    divisors.append(n // k)

        divisors.sort()

        for k in divisors:
            valid = True

            for start in range(0, n, k):
                a = nums[start:start + k]
                b = target[start:start + k]

                # A cyclic rotation of a sorted block has
                # at most one circular descent.
                descents = 0
                for i in range(k):
                    if a[i] > a[(i + 1) % k]:
                        descents += 1
                        if descents > 1:
                            valid = False
                            break

                if not valid:
                    break

                # Exact multiset check using frequency differences
                freq = {}
                for x in a:
                    freq[x] = freq.get(x, 0) + 1

                for x in b:
                    if x not in freq:
                        valid = False
                        break
                    freq[x] -= 1
                    if freq[x] == 0:
                        del freq[x]

                if not valid or freq:
                    valid = False
                    break

            if valid:
                ans += k

        return ans