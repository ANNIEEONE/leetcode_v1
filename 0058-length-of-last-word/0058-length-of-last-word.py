class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        n = len(s)
        count = 0
        i = n-1

        while i>=0:
            if s[i] == ' ':
                break

            count += 1
            i -= 1
        return count
        