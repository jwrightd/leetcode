class Solution {
    public boolean isPalindrome(int x) {
        /*
        int countTens = -1;
        int c = x;
        while (c > 0)
        {
            c = c/10;
            countTens += 1;
        }
        System.out.println(countTens);
        int copy = x;
        long checkPalindrome = 0;
        while (copy > 0)
        {
            int cdigit = copy%10;
            System.out.println(cdigit);
            copy = (copy - cdigit)/10;
            checkPalindrome += cdigit * Math.pow(10, countTens);
            countTens --;
        }
        System.out.print(checkPalindrome);
        return checkPalindrome == x;
        */
        String num = "" + x;
        int len = num.length();
        for (int i = 0; i < len/2; i ++)
        {
            if (num.charAt(i) != num.charAt(len - 1 - i))
            {
                return false;
            }
        }
        return true;
    }
}
