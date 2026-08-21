class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        a,b = Counter(ransomNote), Counter(magazine)
        if a & b == a:
            return True
        return False