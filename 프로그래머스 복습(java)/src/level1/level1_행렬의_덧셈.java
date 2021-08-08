package level1;

import java.util.Arrays;

public class level1_행렬의_덧셈 {
    static class Solution {
        public int[][] solution(int[][] arr1, int[][] arr2) {
            int[][] answer = new int[arr1.length][arr1[0].length];
            for (int i = 0; i < arr1.length; i++) {
                for (int j = 0; j < arr1[0].length; j++) {
                    answer[i][j] = arr1[i][j] + arr2[i][j];
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] arr11 = {{1, 2}, {2, 3}}, arr12 = {{3, 4}, {5, 6}};
        int[][] arr21 = {{1}, {2}}, arr22 = {{3}, {4}};
        System.out.println(Arrays.deepToString(solution.solution(arr11, arr12)));
        System.out.println(Arrays.deepToString(solution.solution(arr21, arr22)));

    }
}
