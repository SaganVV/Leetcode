class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur_sum = nums[0]
        max_sum = nums[0]
        for i, el in enumerate(nums[1::]):
            
            if el>=0:
                if cur_sum < 0:
                    cur_sum = el
                # if cur_sum + el < 0:
                #     cur_sum = el
                else:
                    cur_sum+=el
            elif el<0: 
                if cur_sum+el<0:
                    cur_sum = el
                else:
                    cur_sum += el
            max_sum = max(cur_sum, max_sum)
            #print(el, cur_sum)
            # else:
            #     cur_sum+=el
            
        return max_sum
