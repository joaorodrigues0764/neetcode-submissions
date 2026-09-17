class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False

        s1_count = [0] * 26
        for letter in s1:
            i = ord(letter) - ord('a')
            s1_count[i] += 1
        
        L = len(s1)
        window_count = [0] * 26
        for i in range(L):
            letter = s2[i]
            idx = ord(letter) - ord('a')
            window_count[idx] += 1

        if s1_count == window_count:
            return True

        for i in range(L, len(s2)):
            new_letter = s2[i]
            old_letter = s2[i - L]
            
            idx_new = ord(new_letter) - ord('a')
            idx_old = ord(old_letter) - ord('a')
            
            window_count[idx_new] += 1
            window_count[idx_old] -= 1
            
            if s1_count == window_count:
                return True
        
        return False