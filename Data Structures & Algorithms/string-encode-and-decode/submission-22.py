class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        encoded_string=""
        for s in strs:
            encoded_string+=f"{len(s)}#{s}"
        return encoded_string
    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        encoded_string=[]
        i=0
        while i<len(s):
            j=i
            while s[j]!='#':
                j+=1
            s_len=int(s[i:j])
            encoded_string.append(s[j+1:j+1+s_len])
            i=j+s_len+1
        return encoded_string