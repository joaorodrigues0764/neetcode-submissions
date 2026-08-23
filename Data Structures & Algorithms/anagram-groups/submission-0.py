class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strs_dict = {}
        result = []
        for word in strs:
            sec_list = [0] * 26
            for letter in word:
                position = ord(letter) - ord('a')
                sec_list[position] += 1
            key = tuple(sec_list)
            if key not in strs_dict:
                strs_dict[key] = []
            strs_dict[key] += [word]
        
        return list(strs_dict.values())


            
             
