class Solution:
    def anagramHash(self, s: str) -> tuple:
        count = [0] * 26
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
        
        return tuple(count)

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hMap = {}
        for s in strs:
            hashValStr = self.anagramHash(s)
            if hashValStr in hMap:
                hMap[hashValStr].append(s)
            else: 
                hMap[hashValStr] = [s]
        
        result = []
        for key,val in hMap.items():
            result.append(val)
        
        return result
