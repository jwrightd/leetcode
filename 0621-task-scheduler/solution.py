class Solution(object):
    import heapq

    def leastInterval(self, tasks, n):
        """
        :type tasks: List[str]
        :type n: int
        :rtype: int
        """
        # 26 len array based on alpha
        # need to find number of idles
        # pq

        #new approach, set x = frequency of most common task
        # (x - 1) * (n + 1)
        time = 0
        counter = dict()
        for i in tasks:
            counter[i] = 1 if i not in counter else counter[i] + 1

        heap = []
        cooldown = []

        for i in counter:
            heapq.heappush(heap, -counter[i])

        while len(heap) > 0 or len(cooldown) > 0:
            if len(heap) > 0:
                freq = heapq.heappop(heap)
                if freq + 1 < 0:
                    cooldown.append((freq+ 1, n + time))

            if len(cooldown) > 0:
                a, t = cooldown[0]
                if t == time:
                    cooldown.pop(0)
                    heapq.heappush(heap, a)

            time += 1

        
        return time
