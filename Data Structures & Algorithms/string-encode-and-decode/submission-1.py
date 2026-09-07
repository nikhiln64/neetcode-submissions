class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''
        _str = []
        for s in strs:
            _str.append(str(len(s)))
            _str.append("#")
            _str.append(s)
        return "".join(_str)

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0

        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            l = int(s[i:j])
            i = j+1
            j = i + l
            res.append(s[i:j])
            i = j
        return res
        
        