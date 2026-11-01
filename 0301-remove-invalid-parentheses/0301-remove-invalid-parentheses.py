class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        def is_valid(string):
            balance = 0

            for ch in string:
                if ch == '(':
                    balance += 1
                elif ch == ')':
                    balance -= 1

                    if balance < 0:
                        return False

            return balance == 0

        queue = [s]
        visited = {s}

        while queue:
            result = []

            for current in queue:
                if is_valid(current):
                    result.append(current)

            # Return all valid strings at the first valid BFS level
            if result:
                return result

            next_queue = []

            for current in queue:
                for i in range(len(current)):
                    # Remove parentheses only, not letters
                    if current[i] not in '()':
                        continue

                    new_string = current[:i] + current[i + 1:]

                    if new_string not in visited:
                        visited.add(new_string)
                        next_queue.append(new_string)

            queue = next_queue

        return [""]