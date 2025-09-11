import java.util.*;
class Solution {
    public int lengthOfLongestSubstring(String s) {
        int len = s.length();
        int m = 0;
        for (int i = 0; i < len; i ++)
        {
            HashSet<Character> saved = new HashSet<Character>();
            int count = 0;
            char tmp = s.charAt(i + count);
            //System.out.println(tmp);
            while ((i + count) <= len - 1 && !saved.contains(tmp))
            {
                
                saved.add(tmp);
                count ++;
                tmp = ((i + count) <= len - 1) ? s.charAt(i + count) : tmp;
                //System.out.println(tmp + " " + count);
            }
            m = (count > m) ? count : m;
        }
        return m;
    }
}
