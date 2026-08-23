class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # Last occurrence of every character
        last = {}

        for i, ch in enumerate(s):
            last[ch] = i

        stack = []
        seen = set()

        for i, ch in enumerate(s):

            # Already present in result
            if ch in seen:
                continue

            # Remove bigger characters if they appear again later
            while (
                stack
                and stack[-1] > ch
                and last[stack[-1]] > i
            ):
                removed = stack.pop()
                seen.remove(removed)

            stack.append(ch)
            seen.add(ch)

        return ''.join(stack)