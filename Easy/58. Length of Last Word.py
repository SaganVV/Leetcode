class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        ans = ''
     
        for i in range(len(s)-1, -1, -1):
            if s[i] == ' ':
                if ans:
                    break
            else:
                ans += s[i]
                
        return len(ans)
