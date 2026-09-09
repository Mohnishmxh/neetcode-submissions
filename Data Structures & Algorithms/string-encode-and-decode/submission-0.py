class Solution:
    def encode(self, strs: list[str]) -> str:
        encoded_parts = []
        for s in strs:
            encoded_parts.append(f"{len(s)}#{s}")
        return "".join(encoded_parts)

    def decode(self, s: str) -> list[str]:
        res = []
        i = 0
        
        while i < len(s):
            
            j = s.find('#', i)
            
            length = int(s[i:j])
            
            start = j + 1
            end = start + length
            res.append(s[start:end])
            
            i = end
            
        return res