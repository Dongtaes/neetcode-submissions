class Solution:
    def encode(self, strs: List[str]) -> str:
        self.n = len(strs)
        if strs == [""]: return ""
        else:
            self.count = []
            msg = []
            for s in strs:
                msg.append(s)
                self.count.append(len(s))
            return"".join(msg)

    def decode(self, s: str) -> List[str]:
        res = []
        if s == "":
            for i in range(self.n):
                res.append("")
            return res
        else:
            i = 0
            j = 0
            for c in self.count:
                j += c
                res.append(s[i:j])
                i += c
        return res
