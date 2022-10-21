class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        letters_hash = {}
        for i in range(len(s)):
            letter_s = s[i]
            letter_t = t[i]
            if letter_s in letters_hash:
                if letters_hash[letter_s] != letter_t:
                    return False
            else:
                if letter_t in letters_hash.values():
                    return False
                letters_hash[letter_s] = letter_t
        return True