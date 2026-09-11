class Solution(object):
    def totalNumbers(self, digits):
        """
        :type digits: List[int]
        :rtype: int
        """
        output = set()
        visited = set()
        freq = defaultdict(int)
        for i in digits:
            freq[str(i)] += 1
        N = len(digits)
        def dfs(num):
            if len(num) == 3:
                if num[-1] in ["0", "2", "4", "6", "8"]:
                    output.add(num)
                return
            if num in visited:
                return
            visited.add(num)
            for child in freq:
                if freq[child] == 0:
                    continue
                if len(num) == 0 and child == "0":
                    continue
                newNum = num + child
                freq[child] -= 1
                dfs(newNum)
                freq[child] += 1
            

        dfs("")
        return len(output)
        
