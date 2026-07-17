class Solution(object):
    def fullJustify(self, words, maxWidth):
        output = []
        currLine = []
        i = 0
        n = len(words)
        currWidth = 0
        while i < n:
            while currWidth < maxWidth and i < n:
                cLen = len(words[i])
                if currWidth + cLen <= maxWidth:
                    currLine.append(words[i])
                    currWidth += cLen + 1 #space after every
                    i += 1
                else:
                    break
            currWidth -= 1 # take last space
            tmp = []
            lenLine = len(currLine)
            toAlloc = maxWidth - currWidth
            gaps = lenLine - 1

            if i == n: # we are on last line
                for val in currLine:
                    tmp.append(val + " ")
                line = "".join(tmp).strip() + " " * (maxWidth - currWidth)
                output.append(line)
            else:
                for val in currLine:
                    if lenLine == 1:
                        tmp.append(val + " " * (maxWidth - currWidth))
                    elif gaps != 0:
                        numSpace = toAlloc // (gaps) if toAlloc % (gaps) == 0 else toAlloc // (gaps) + 1
                        toAlloc -= numSpace
                        gaps -= 1
                        tmp.append(val + " " * (numSpace + 1))                 
                    else:
                        tmp.append(val)
                output.append("".join(tmp))
                currWidth = 0
                currLine = []
        return output
