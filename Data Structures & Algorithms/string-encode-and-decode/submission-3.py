class Solution:

    def encode(self, strs: List[str]) -> str:
        return ''.join(f"{len(s)}#{s}" for s in strs)


    def decode(self, s: str) -> List[str]:
        start_num = ""
        decoded = []
        i = 0
        while i < len(s):
            if s[i] != "#":
                start_num += s[i]
            else:
                decoded.append(s[i+1:i+1+int(start_num)])
                i = i+int(start_num)
                start_num = ""
            i+=1
        return decoded


