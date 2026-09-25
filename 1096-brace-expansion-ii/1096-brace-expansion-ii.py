class Solution:
    def braceExpansionII(self, expression: str):
        def parse(i):
            result = set()
            current = {""}

            while i < len(expression) and expression[i] != '}':
                ch = expression[i]

                if ch == ',':
                    # Union
                    result |= current
                    current = {""}
                    i += 1

                elif ch == '{':
                    # Parse expression inside braces
                    inside, i = parse(i + 1)

                    # Concatenate current with inside
                    current = {
                        a + b
                        for a in current
                        for b in inside
                    }

                else:
                    # Normal lowercase letter
                    current = {
                        word + ch
                        for word in current
                    }
                    i += 1

            # Add the last part
            result |= current

            # Skip '}'
            if i < len(expression) and expression[i] == '}':
                i += 1

            return result, i

        result, _ = parse(0)

        return sorted(result)