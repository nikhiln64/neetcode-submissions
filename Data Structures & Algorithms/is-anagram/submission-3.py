class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        hashMap = {}

        for c in range(len(s)):
            hashMap[s[c]] = hashMap.get(s[c], 0) + 1
        
        for c in range(len(t)):
            if t[c] not in hashMap:
                return False
            hashMap[t[c]] =  hashMap.get(t[c]) - 1
            if hashMap[t[c]] == 0:
                del hashMap[t[c]]

        return len(hashMap) == 0