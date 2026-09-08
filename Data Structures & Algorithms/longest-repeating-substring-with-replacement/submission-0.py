class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        dict_letters = {}
        left = 0  
        result = 0  
        for right in range(len(s)):
            if s[right] in dict_letters:
                dict_letters[s[right]] += 1
            else:
                dict_letters[s[right]] = 1
            while (right - left + 1) - max(dict_letters.values()) > k:
                dict_letters[s[left]] -= 1
                left += 1
            result = max(result, right - left + 1)
        return result