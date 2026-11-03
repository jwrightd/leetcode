class Solution(object):
    def wordPattern(self, pattern, s):
        words = s.split(" ")
        if len(pattern) != len(words):
            return False
        mapping = {}
        used = set()
        for idx, ch in enumerate(pattern):
            if ch not in mapping:
                if words[idx] in used:
                    return False
                mapping[ch] = words[idx]
                used.add(words[idx])
            else:
                if mapping[ch] != words[idx]:
                    return False
        return True
