package level1;

import java.util.*;

public class level1_실패율 {
    static class Solution {
        public int[] solution(int N, int[] stages) {
            int[] answer = new int[N];
            double[][] result = new double[N][2];
            int people = stages.length;
            for (int stage = 1; stage < N + 1; stage++) {
                int count = 0;
                if (people != 0) {
                    for (int j : stages) {
                        if (j == stage) {
                            count += 1;
                        }
                    }
                    result[stage - 1][0] = stage;
                    result[stage - 1][1] = (double) count / (double) people;
                    people -= count;
                } else {
                    result[stage - 1][0] = stage;
                    result[stage - 1][1] = 0;
                }
            }

            Arrays.sort(result, (a, b) -> Double.compare(b[1], a[1]));
            for (int i = 0; i < result.length; i++) {
                answer[i] = (int) result[i][0];
            }

            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n1 = 5, n2 = 4;
        int[] stages1 = {2, 1, 2, 6, 2, 4, 3, 3};
        int[] stages2 = {4, 4, 4, 4, 4};
        System.out.println(Arrays.toString(solution.solution(n1, stages1)));
        System.out.println(Arrays.toString(solution.solution(n2, stages2)));
    }
}
