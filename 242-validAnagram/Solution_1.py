class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        Hash_s = {}
        Hash_t = {}

        for i in range(len(s)):
            Hash_s[s[i]] = Hash_s.get(s[i], 0) + 1
            Hash_t[t[i]] = Hash_t.get(t[i], 0) + 1

        return Hash_s == Hash_t


solution = Solution()
print(solution.isAnagram("anagram", "nagaram"))
print(solution.isAnagram("rat", "car"))
