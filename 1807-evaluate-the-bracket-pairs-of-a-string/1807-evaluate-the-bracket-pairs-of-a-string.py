class Solution:
    def evaluate(self, s: str, knowledge) -> str:
        # Convert knowledge into a dictionary
        values = {key: value for key, value in knowledge}

        result = []
        i = 0

        while i < len(s):

            if s[i] == '(':
                i += 1
                start = i

                # Find closing bracket
                while s[i] != ')':
                    i += 1

                key = s[start:i]

                # Replace with value or '?'
                result.append(values.get(key, '?'))

                i += 1

            else:
                result.append(s[i])
                i += 1

        return ''.join(result)