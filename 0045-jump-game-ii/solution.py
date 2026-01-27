class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums) - 1

        visited = set()
        q = []
        vtx = (0, 0)
        q.append(vtx)
        visited.add(vtx)

        while len(q) > 0:
            vtx = q.pop(0)
            num, count = vtx
            if num == n:
                return count
            possibles = [i + num for i in range(1, nums[num] + 1)]
            for i in possibles:
                if i not in visited:
                    q.append((i, count + 1))
                    visited.add(i)
            

    
        
#BFS
