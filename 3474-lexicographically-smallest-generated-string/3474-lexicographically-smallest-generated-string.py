class Solution:
    def generateString(self, str1: str, str2: str) -> str:
        n = len(str1)
        m = len(str2)
        L = n + m - 1
        
        word = [None] * L
        is_fixed = [False] * L
        
        # Step 1: Enforce all 'T' conditions
        for i in range(n):
            if str1[i] == 'T':
                for j in range(m):
                    pos = i + j
                    if word[pos] is not None and word[pos] != str2[j]:
                        return ""  # Conflict between 'T' constraints
                    word[pos] = str2[j]
                    is_fixed[pos] = True
        
        # Step 2: Fill remaining positions with 'a' (lexicographically smallest)
        for i in range(L):
            if word[i] is None:
                word[i] = 'a'
        
        # Step 3: Enforce all 'F' conditions
        # Convert to list of characters for easy comparison and mutation
        for i in range(n):
            if str1[i] == 'F':
                # Check if word[i .. i + m - 1] currently matches str2
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                
                if match:
                    # We must change at least one character in this window.
                    # Find the rightmost character in [i, i + m - 1] that is NOT fixed.
                    changed = False
                    for pos in range(i + m - 1, i - 1, -1):
                        if not is_fixed[pos]:
                            # Find the smallest character different from str2[pos - i]
                            # Since it currently matches, word[pos] == str2[pos - i]
                            for c in range(ord('a'), ord('z') + 1):
                                ch = chr(c)
                                if ch != str2[pos - i]:
                                    word[pos] = ch
                                    changed = True
                                    break
                            if changed:
                                break
                    
                    if not changed:
                        # All characters in the window are fixed by 'T'
                        return ""
        
        # Step 4: Final verification of all 'F' constraints
        # Changing a character to break one 'F' could theoretically cause a match elsewhere
        for i in range(n):
            if str1[i] == 'F':
                match = True
                for j in range(m):
                    if word[i + j] != str2[j]:
                        match = False
                        break
                if match:
                    return ""
        
        return "".join(word)