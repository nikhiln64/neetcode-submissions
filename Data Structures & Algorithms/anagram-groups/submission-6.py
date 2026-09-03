class Solution:

    def getKey(self, s: str) -> int:
        count = [0] * 26

        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}

        for s in strs:
            strMap.setdefault(self.getKey(s), []).append(s)
        
        result = []

        for l in strMap.values():
            result.append(l)

        return result
