class Solution:
    def isPalindrome(self, s: str) -> bool:
        alfnum = {'a','b','c','d','e','f','g','h', 'i', 'j', 'k', 'l', 'm', 'n', 'o','p','q','r','s','t','u','v','w','x','y','z', '1','2','3','4','5','6','7','8','9','0'}
        cor_st = ''
        for ch in s:
            x =ch.lower()
            if x in alfnum:
                cor_st+=x
        n = len(cor_st)
        for i in range(n):
            if cor_st[i] != cor_st[n-i-1]:
                return False
        return True
