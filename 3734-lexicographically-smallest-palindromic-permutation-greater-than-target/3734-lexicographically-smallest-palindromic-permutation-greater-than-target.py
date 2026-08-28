from collections import Counter

class Solution:
    def lexPalindromicPermutation(self, s: str, target: str) -> str:
        n = len(s)
        m = n // 2
        count = Counter(s)
        
        # Check if a palindrome can be formed
        odd_chars = [ch for ch, cnt in count.items() if cnt % 2 != 0]
        if len(odd_chars) > 1:
            return ""
        
        mid_char = odd_chars[0] if odd_chars else ""
        half_pool = Counter({ch: cnt // 2 for ch, cnt in count.items()})
        
        # 1. Try exact prefix match: P[:m] == target[:m]
        target_prefix_pool = Counter(target[:m])
        can_match_prefix = all(half_pool[ch] >= target_prefix_pool[ch] for ch in target_prefix_pool)
        
        if can_match_prefix:
            p0 = target[:m] + mid_char + target[:m][::-1]
            if p0 > target:
                return p0
                
        # 2. Find the smallest prefix of length m strictly greater than target[:m]
        curr_pool = Counter()
        for i in range(m):
            curr_pool[target[i]] += 1
            
        for i in range(m - 1, -1, -1):
            curr_pool[target[i]] -= 1
            
            # Check if target[:i] can be formed
            if all(half_pool[ch] >= curr_pool[ch] for ch in curr_pool):
                rem_pool = half_pool - curr_pool
                
                # Find the smallest character greater than target[i]
                valid_chars = sorted(ch for ch in rem_pool.elements() if ch > target[i])
                if valid_chars:
                    chosen_char = valid_chars[0]
                    rem_pool[chosen_char] -= 1
                    
                    # Form prefix: target[:i] + chosen_char + sorted(remaining)
                    rem_chars = "".join(sorted(rem_pool.elements()))
                    prefix = target[:i] + chosen_char + rem_chars
                    
                    return prefix + mid_char + prefix[::-1]
                    
        return ""