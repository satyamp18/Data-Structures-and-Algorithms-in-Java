from collections import Counter


class Solution:

  def uncommonFromSentences(self, s1: str, s2: str) -> list[str]:
    # Combine both sentences and count occurrences of every word
    counts = Counter((s1 + " " + s2).split())

    # A word is uncommon if its total frequency across both sentences is exactly 1
    return [word for word, count in counts.items() if count == 1]