package level2;

import java.util.Arrays;

public class level2_피보나치_수 {
    static class Solution {
        public int solution(int n) {
            int[] answer = new int[n + 1];
            answer[0] = 0;
            answer[1] = 1;
            int x = 2;
            while (x != n + 1) {
                answer[x] = (answer[x - 1] + answer[x - 2]) % 1234567;
                x++;
            }
            return answer[n];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(3));
        System.out.println(solution.solution(5));
    }
}
