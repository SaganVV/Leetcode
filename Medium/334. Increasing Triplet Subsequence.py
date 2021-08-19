class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        min1 = min2 = float('inf')
        for n in nums:
            print(min1, min2, n)
            if n<min1:
                min1 = n
            elif min1<n<min2:
                min2 = n
            elif n>min2:
                return True
        return False
"""Firstly, we find 2 minimum current value. If the next number less then first, we can put this number at min1 because answer cant change fater this operation
(if increasing triplet exist like num1<num2<num3 then if we have num4 < num1, then num4<num2<num3; If num1<num2 and num4<num1 and we have found num3: num4<num2<num3
=> num1<num2<num3 and such triplet exist)"""
