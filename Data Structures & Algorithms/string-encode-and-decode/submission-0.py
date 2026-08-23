class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded_string = ""
        for word in strs:
            len_word = len(word)
            encoded_string += str(len_word) + "#" + word

        return encoded_string

    def decode(self, s: str) -> List[str]:
        len_s = len(s)
        decoded_strs = []
        i = 0
        while i < len_s:
            j = i
            while s[j] != "#":
                j += 1
            size = int(s[i:j])
            word = s[j + 1 : j + 1 + size]
            decoded_strs.append(word)
            i = j + 1 + size

        return decoded_strs
