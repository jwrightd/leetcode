class Solution(object):
    def findTheWinner(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        count = -1
        queue = [i for i in range(1, n + 1)]
        while len(queue) > 1:
            count += k
            count %= len(queue)
            queue.pop(count)
            count -= 1

        return queue[0]
