class Solution(object):
    def canReorderDoubled(self, arr):
        """
        :type arr: List[int]
        :rtype: bool
        """
        arr.sort()
        print(arr)
        # we want to see if we can arrange in doubled pairs
        # well this seems like every num needs a pair, and it can either be the small or large val
        # lets consider the smallest number
        # this can only be smallest number, and so it must be paired with twice itself if posiitve
        # or half itself if negative

        # so lets do freq dict of our nums
        # then go from least to greatest, subtracting freq as we process each number. if we ever cant match, ret false

        counter = {}
        for i in arr:
            counter[i] = 1 if i not in counter else counter[i] + 1
        
        for num in arr: #should be sorted
            #print(counter)
            if num < 0: #each we treat as smallest
                target = float(num) / 2             
                #print(num, target)
            elif num > 0:
                target = 2 * num   
                #print(num, target)        
            else: #num == 0
                target = 0
                if counter[0] % 2 == 1:
                    return False
            if counter[num] == 0:
                continue
            if target not in counter or counter[target] < counter[num]:
                return False
            counter[target] -= counter[num]
            counter[num] = 0
            
        return True
