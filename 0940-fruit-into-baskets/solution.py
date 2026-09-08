class Solution(object):
    def totalFruit(self, fruits):
        """
        :type fruits: List[int]
        :rtype: int
        """
        left = 0
        N = len(fruits)
        longestWindow = float('-inf')
        numFruits = 0
        freqs = defaultdict(int)
        for right in range(N):
            fruit = fruits[right]
            freqs[fruit] += 1
            if freqs[fruit] == 1:
                numFruits += 1
            while numFruits > 2:
                freqs[fruits[left]] -= 1
                if freqs[fruits[left]] == 0:
                    numFruits -= 1
                left += 1
            longestWindow = max(longestWindow, right - left + 1)
        return longestWindow





        
