class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strMap = {}

        for s in strs:
            count = [0] * 26
            for i in range(len(s)):
                count[ord(s[i]) - ord('a')] += 1
            strMap.setdefault(tuple(count), []).append(s)
        
        result = []

        return list(strMap.values())
