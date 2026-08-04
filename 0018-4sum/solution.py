class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        # should memo 2
        # chcek others
        valids = []
        N = len(nums)
        # dict: target --> list of (a, b) idx tuples
        nums.sort()
        for i in range(N):
            for j in range(i + 1, N):
                left = j + 1
                right = N - 1
                curr = nums[i] + nums[j]
                #print(curr, left, right)
                while left < right:
                    if curr + nums[left] + nums[right] > target:
                        right -= 1
                    elif curr + nums[left] + nums[right] == target:
                        if [nums[i], nums[j], nums[left], nums[right]] not in valids:
                            valids.append([nums[i], nums[j], nums[left], nums[right]])
                        right -=1
                        left += 1
                    else:
                        left += 1
               # print(left, right, N)
                #if left < N and right < N and left != right and curr + nums[left] + nums[right] == target:
                    

        return valids
        
