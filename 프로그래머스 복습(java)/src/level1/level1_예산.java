package level1;

import java.util.Arrays;

public class level1_예산 {
    static class Solution {
        public int solution(int[] d, int budget) {
            int answer = 0;
            Arrays.sort(d);
            for (int i = 0; i < d.length; i++) {
                budget -= d[i];
                if (budget >= 0) {
                    answer++;
                } else {
                    break;
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] d1 = {1, 3, 2, 5, 4}, d2 = {2, 2, 3, 3};
        int budget1 = 9, budget2 = 10;
        System.out.println(solution.solution(d1, budget1));
        System.out.println(solution.solution(d2, budget2));
    }
}
