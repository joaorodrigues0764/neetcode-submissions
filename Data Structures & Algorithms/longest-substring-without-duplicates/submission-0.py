class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        dict_s ={}
        result = 0
        start = 0
        end = 0
        
        for character in s:
            if character in dict_s and dict_s[character] >= start:
                start = dict_s[character] + 1
            
            dict_s[character] = end
            result = max(result, end - start + 1)

            end += 1
        return result