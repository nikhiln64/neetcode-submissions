class Solution:

    def encode(self, strs: List[str]) -> str:
        if strs == []:
            return ''

        _strs = []
        for s in strs:
            _strs.append(str(len(s)))
            _strs.append("#")
            _strs.append(s)
        return "".join(_strs)
           

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



