class Solution:
    def climbStairs(self, n: int) -> int:
        f = (1, 2)
        if n<=2:
            return f[n-1]
        a, b = f
        for i in range(2, n+1):
            a, b = b, a+b
        return a
