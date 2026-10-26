class Solution:
    def addOperators(self, num: str, target: int) -> list[str]:
        result = []
        n = len(num)

        def backtrack(index, expression, value, last_operand):
            if index == n:
                if value == target:
                    result.append(expression)
                return

            for end in range(index, n):
                # Avoid numbers with leading zeros
                if end > index and num[index] == '0':
                    break

                operand = int(num[index:end + 1])

                if index == 0:
                    # First number: no operator needed
                    backtrack(
                        end + 1,
                        str(operand),
                        operand,
                        operand
                    )
                else:
                    # Addition
                    backtrack(
                        end + 1,
                        expression + '+' + str(operand),
                        value + operand,
                        operand
                    )

                    # Subtraction
                    backtrack(
                        end + 1,
                        expression + '-' + str(operand),
                        value - operand,
                        -operand
                    )

                    # Multiplication: handle operator precedence
                    backtrack(
                        end + 1,
                        expression + '*' + str(operand),
                        value - last_operand + last_operand * operand,
                        last_operand * operand
                    )

        backtrack(0, "", 0, 0)
        return result