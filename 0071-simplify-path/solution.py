class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        
        # this is stack i think
        directories = path.split("/")
        directories = [i for i in directories if i != ""]
        stk = []
        for i in directories:
            if i == ".":
                continue
            if i == "..":
                if stk:
                    stk.pop(-1)
            else:
                stk.append(i)
        return "/" + "/".join(stk)
