class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []

        for ch in s:
            if ch == '(':
                # Start a new substring
                stack.append(ch)

            elif ch == ')':
                # Collect everything until '('
                temp = []

                while stack[-1] != '(':
                    temp.append(stack.pop())

                # Remove '('
                stack.pop()

                # Put reversed substring back
                stack.extend(temp)

            else:
                stack.append(ch)

        return ''.join(stack)