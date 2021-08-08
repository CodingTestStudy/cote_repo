package level1;

import java.util.Arrays;

public class level1_x만큼_간격이_있는_n개의_숫자 {
    static class Solution {
        public long[] solution(int x, int n) {
            long[] answer = new long[n];
            for (int i = 1; i <= n; i++) {
                answer[i - 1] = (long) x * i;
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(2, 5)));
        System.out.println(Arrays.toString(solution.solution(4, 3)));
        System.out.println(Arrays.toString(solution.solution(-4, 2)));
    }
}
