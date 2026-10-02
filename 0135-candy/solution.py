class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        # well theoretically you need a diff number for each different rating?
        # check both neighbors
        N = len(ratings)
        if N == 1:
            return 1
            
        candies = [1 for _ in range(N)]
        for i in range(1, N):
            if ratings[i - 1] < ratings[i]:
                candies[i] = candies[i - 1] + 1

        for i in range(N - 2, -1, -1):
            if ratings[i + 1] < ratings[i]:
                candies[i] = max(candies[i], candies[i + 1] + 1)

        return sum(candies)
