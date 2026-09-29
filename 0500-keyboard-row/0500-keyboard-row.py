class Solution:
    def findWords(self, words):
        rows = [
            set("qwertyuiop"),
            set("asdfghjkl"),
            set("zxcvbnm")
        ]

        result = []

        for word in words:
            w = word.lower()

            for row in rows:
                if all(ch in row for ch in w):
                    result.append(word)
                    break

        return result