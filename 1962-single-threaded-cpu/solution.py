class Solution(object):
    def getOrder(self, tasks):
        """
        :type tasks: List[List[int]]
        :rtype: List[int]
        """
        import heapq
        # should just be a heap here
        # index on [processing time, index, starting time]

        #algorithm
        #first sort tasks -- so earlier start is first
        newTasks = []
        c = 0
        for s, p in tasks:
            newTasks.append([s, p, c])
            c += 1
        tasks = newTasks
        tasks.sort()

        order = []

        currTime = 0
        heap = []

        idx = 0
        N = len(tasks)
        while idx < N or heap:

            if not heap and tasks[idx][0] > currTime:
                currTime = tasks[idx][0]
            
            while idx < N and tasks[idx][0] <= currTime:
                heapq.heappush(heap, [tasks[idx][1], tasks[idx][2]])
                idx += 1
            
            proc, ind = heapq.heappop(heap)
            order.append(ind)
            currTime += proc
        return order
        
