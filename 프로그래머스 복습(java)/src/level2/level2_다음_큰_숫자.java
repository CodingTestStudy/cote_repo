package level2;

public class level2_다음_큰_숫자 {
    static class Solution {

        //More Simple Code
        public int nextBigNumber(int n)
        {
            int a = Integer.bitCount(n);
            int compare = n+1;

            while(true) {
                if(Integer.bitCount(compare)==a)
                    break;
                compare++;
            }

            return compare;
        }


        public int solution(int n) {
            int one = getOne(n);

            for (int num = n + 1; num <= 1000000; num++) {
                if (one == getOne(num)) {
                    return num;
                }
            }
            return 1000000;
        }

        private int getOne(int n) {
            int one = 0;
            String s = Integer.toBinaryString(n);
            char[] c = s.toCharArray();
            for (char c1 : c) {
                if (c1 == '1') {
                    one++;
                }
            }
            return one;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(78));
        System.out.println(solution.solution(15));
    }
}
