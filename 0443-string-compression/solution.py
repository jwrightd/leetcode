class Solution:
    def compress(self, chars: List[str]) -> int:
        # constant extra space
        # we just have a pointer for the char we are processing, a the idx we are editing, and then a number of the letter count
        processing = 0
        editing = 0
        count = 0
        current = None
        n = len(chars) 
        while processing < n:
            if current == None:
                current = chars[0]
                editing += 1
                count += 1
            else:
                if chars[processing] == current:
                    count += 1
                else:
                    chars[editing - 1] = current
                    if count != 1:
                        
                        strCount = str(count)
                        for i in range(len(strCount)):
                            chars[editing] = strCount[i]
                            #print(chars[editing], editing, current)
                            #count = count // 10
                            editing += 1
                    current = chars[processing]
                    count = 1
                    editing += 1
            processing += 1
        strCount = str(count)
        chars[editing - 1] = current
        if count == 1:
            return editing
        #print(chars)
        for i in range(len(strCount)):
            if editing == n:
                break
            chars[editing] = strCount[i]
            #count = count // 10
            editing += 1
        return editing


