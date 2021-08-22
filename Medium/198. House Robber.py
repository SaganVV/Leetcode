class Solution:
    def rob(self, nums: List[int]) -> int:
        max_money = [0, nums[0]]
        numb_last_house = 0
        for i in range(1, len(nums)):
            if i-1 == numb_last_house:
                max_with_cur_house = max_money[-2]+nums[i]
                if max_with_cur_house > max_money[-1]:
                    max_money.append(max_with_cur_house)
                    numb_last_house = i
                else:              
                    max_money.append(max_money[-1])
            else:
                
                max_money.append(max_money[-1]+nums[i])
                numb_last_house = i
           # print(i, max_money, nums)  
        return max_money[-1]
# Used dynamic programming approach. At the "numb_last_house" i keep number of the last house, what was robed at best solution at processing dynumic programming
# max_money[i] - its max money, that we can rob from first "i" house
# Other we can understand from code

# Time complexity: O(n)
# Space complexity: O(n) 

#We can do better. For this we can keep at max_money only last two values (because only them can 
