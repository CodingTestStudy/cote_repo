package level1;

import java.util.Arrays;

public class level1_하샤드_수 {
    static class Solution {
        public boolean solution(int x) {
            String s = String.valueOf(x);
            int sum_value = 0;
            for (int i = 0; i < s.length(); i++) {
                sum_value += Integer.parseInt(s.substring(i, i + 1));
            }
            return x % sum_value == 0;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(10));
        System.out.println(solution.solution(12));
        System.out.println(solution.solution(11));
        System.out.println(solution.solution(13));
    }
}
