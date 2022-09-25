def longestPalindrome(s: str) -> int:
        char_count = {}
        max_len = 0
        for char in s:
            if char not in char_count:
                char_count[char] = 1
            else:
                char_count[char] += 1
        for counts in char_count.values():
            max_len += counts // 2 * 2
            if max_len % 2 == 0 and counts % 2 == 1:
                max_len += 1
        return max_len