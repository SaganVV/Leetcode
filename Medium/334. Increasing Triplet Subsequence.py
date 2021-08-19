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
