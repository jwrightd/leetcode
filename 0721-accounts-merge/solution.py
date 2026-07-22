class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        # could also dfs from all unvisited emails, this checks number of components
        # then we can just see the name assoc to some list of emails in o(1) time after o(n) memo
        output = []
        visited = set()
        edges = {}
        emailToName = {}
        for acc in accounts:
            name = acc[0]
            first = acc[1]
            emailToName[first] = name
            if first not in edges:
                edges[first] = [] 
            for email in acc[2:]:
                if email not in edges:
                    edges[email] = []
                edges[first].append(email)
                edges[email].append(first)
                emailToName[email] = name
        seen = []
        def dfs(node):
            if node in visited:
                return
            visited.add(node)
            seen.append(node)
            for child in edges[node]:
                dfs(child)
        
        for email in edges:
            if email not in visited:
                dfs(email)
                firstEmail = seen[0]
                seen.sort()
                output.append([emailToName[firstEmail]] + seen)
                seen = []
        return output
        

