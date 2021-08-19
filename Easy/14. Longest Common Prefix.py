class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = ''
        
        for i in range(256):
            try:
                symbols = {j[i] for j in strs}
                if len(symbols)==1:
                    pref += strs[0][i]
                else:
                    return pref
            except:
                return pref
