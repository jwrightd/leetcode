class Solution(object):
    def maxArea(self, height):
        left = 0
        right = len(height) - 1
        high = -1
        while (right > left):
            tmp = (right - left) * min(height[right], height[left])
            high = tmp if tmp > high else high
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        return high

        """
        for i in range(0, length):
            for j in range(i + 1, length):
                tmp = (j - i) * min([height[i], height[j]])
                high = tmp if high < tmp else high
        return high
        :type height: List[int]
        :rtype: int
        """
        
