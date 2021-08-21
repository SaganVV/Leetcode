class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_part = [1]
        left = 1
       # right_part = [1]
        
        n = len(nums)
        ans = [0]*n
        for el in nums[:-1]:
            left*=el
            left_part.append(left)
        left = 1

        for i, el in enumerate(reversed(nums[1:])):
            #ans.append(right*left_part[n-i-1])
            ans[i] = left*left_part.pop()
            left*=el
           # right_part.append(right)
            #ans.append(right*left_part[i])

        ans[n-1] = left

        return ans[::-1]
