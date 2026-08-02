class Solution(object):
    def uniqueEmailGroups(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        stuff = set()
        for email in emails:
            idx = email.index("@")
            localname = email[:idx]
            if "+" in localname:
                localname = localname[:localname.index("+")]
            localname = list(localname.lower())
            fixed = []
            for i in localname:
                if i != ".":
                    fixed.append(i)
            final = "".join(fixed)


            domain = email[idx:].lower()
            stuff.add(final + domain)
        return len(stuff)
        
