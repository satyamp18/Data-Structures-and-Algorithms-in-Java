class Solution:
    def decodeString(self, s: str) -> str:
        num_stack = []
        str_stack = []

        curr = ""
        num = 0

        for ch in s:

            if ch.isdigit():
                num = num * 10 + int(ch)

            elif ch == '[':
                # Save current string and repeat count
                num_stack.append(num)
                str_stack.append(curr)

                # Reset for inside the brackets
                num = 0
                curr = ""

            elif ch == ']':
                # Get repeat count
                repeat = num_stack.pop()

                # Get string before '['
                prev = str_stack.pop()

                curr = prev + curr * repeat

            else:
                curr += ch

        return curr