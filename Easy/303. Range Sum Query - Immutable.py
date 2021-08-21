class NumArray:

    def __init__(self, nums: List[int]):
        self.array = nums.copy()
        self.__left_sum = [0]
        for el in nums[:-1]:
            self.__left_sum.append(self.__left_sum[-1]+el)
        
        self.__right_sum = [0]
        for el in reversed(nums[1::]):
            self.__right_sum.append(self.__right_sum[-1]+el)
        self.__right_sum.append(self.__right_sum[-1]+nums[0])
        self.__right_sum = self.__right_sum[::-1]
        self.sum_array = sum(nums)
    def sumRange(self, left: int, right: int) -> int:
        return self.sum_array-self.__left_sum[left]-self.__right_sum[right+1]
