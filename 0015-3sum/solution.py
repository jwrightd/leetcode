class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        ret = []
        n = len(nums)
        for i in range(n - 2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            goal = -nums[i]
            p1 = i + 1
            p2 = n - 1
            while p2 > p1:
                tmp = nums[p1] + nums[p2]
                if tmp == goal:
                    ret.append([nums[i], nums[p1], nums[p2]])
                    p1n = nums[p1]
                    p2n = nums[p2]
                    p2 -=1
                    p1 += 1
                    while p1 < p2 and nums[p1] == p1n:
                        p1 += 1
                    while p2 > p1 and nums[p2] == p2n:
                        p2 -=1
                elif tmp > goal:
                    p2 -= 1
                else:
                    p1 += 1
        return ret
            
        
