class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s) == 0:
            return ""
        maxLen = 1
        start = 0
        for i in range(1, len(s)):
        # Expand around the center character
            l = i - 1
            r = i
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    start = l
                    maxLen = r - l + 1
                l -= 1
                r += 1

        # Expand around the center two characters
            l = i - 1
            r = i + 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r - l + 1 > maxLen:
                    start = l
                    maxLen = r - l + 1
                l -= 1
                r += 1
        return s[start:start + maxLen]