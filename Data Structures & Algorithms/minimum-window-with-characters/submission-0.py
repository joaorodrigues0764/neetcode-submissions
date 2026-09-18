from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""

        # Target counts and window trackers
        t_count = Counter(t)
        window_s = Counter()
        have, need = 0, len(t_count)
        
        left = 0
        res_len, res_start = -1, 0

        # Expand the window using the right pointer
        for right, char in enumerate(s):
            window_s[char] += 1

            if char in t_count and window_s[char] == t_count[char]:
                have += 1

            # Shrink the window while it is valid
            while have == need:
                window_size = right - left + 1
                if res_len == -1 or window_size < res_len:
                    res_len, res_start = window_size, left

                # Remove the left character to find a smaller valid window
                left_char = s[left]
                window_s[left_char] -= 1
                if left_char in t_count and window_s[left_char] < t_count[left_char]:
                    have -= 1
                
                left += 1

        if res_len == -1:
            return ""
        
        return s[res_start : res_start + res_len]