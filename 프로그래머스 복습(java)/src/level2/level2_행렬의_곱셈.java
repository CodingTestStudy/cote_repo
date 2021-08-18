package level2;

import java.util.Arrays;

public class level2_행렬의_곱셈 {
    static class Solution {
        public int[][] solution(int[][] arr1, int[][] arr2) {
            int arr1Row = arr1.length;
            int arr1Column = arr1[0].length;
            int arr2Row = arr2.length;
            int arr2Column = arr2[0].length;

            int[][] answer = new int[arr1Row][arr2Column];
            for (int i = 0; i < arr1Row; i++) {
                for (int j = 0; j < arr2Column; j++) {
                    for (int k = 0; k < arr1Column; k++) {
                        answer[i][j] += arr1[i][k] * arr2[k][j];
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] arr11 = {{1, 4}, {3, 2}, {4, 1}};
        int[][] arr12 = {{3, 3}, {3, 3}};
        int[][] arr21 = {{2, 3, 2}, {4, 2, 4}, {3, 1, 4}};
        int[][] arr22 = {{5, 4, 3}, {2, 4, 1}, {3, 1, 1}};
        System.out.println(Arrays.deepToString(solution.solution(arr11, arr12)));
        System.out.println(Arrays.deepToString(solution.solution(arr21, arr22)));
    }
}
