class Solution:
    def search(self, nums: List[int], target: int) -> int:
     #   ans = -1
        l = 0 
        r = len(nums)-1
        while l<=r:
            point = (l+r)//2
            val = nums[point]
            
            if val == target:
                return point
            elif target < val:
                r = point-1
            else:
                l = point+1
        return -1
