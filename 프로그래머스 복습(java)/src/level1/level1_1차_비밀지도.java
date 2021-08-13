package level1;

import java.util.Arrays;

public class level1_1차_비밀지도 {
    static class Solution {
        public String[] solution(int n, int[] arr1, int[] arr2) {
            String[] answer = new String[n];
            String[][] map1 = new String[n][n];
            String[][] map2 = new String[n][n];
            makeMap(n, arr1, map1);
            makeMap(n, arr2, map2);

            for (int i = 0; i < n; i++) {
                String ans = "";
                for (int j = 0; j < n; j++) {
                    if (map1[i][j].equals("#") || map2[i][j].equals("#")) {
                        ans += "#";
                    } else {
                        ans += " ";
                    }
                }
                answer[i] = ans;
            }
            return answer;
        }

        private void makeMap(int n, int[] arr, String[][] map) {
            for (int i = 0; i < n; i++) {
                StringBuilder sb = new StringBuilder(Integer.toBinaryString(arr[i]));
                sb.reverse();
                fillZeroAtFront(n, sb);
                sb.reverse();
                for (int j = 0; j < n; j++) {
                    if (sb.charAt(j) == '1') {
                        map[i][j] = "#";
                    } else {
                        map[i][j] = " ";
                    }
                }
            }
        }

        private void fillZeroAtFront(int n, StringBuilder sb) {
            if (sb.length() != n) {
                int count = n - sb.length();
                sb.append("0".repeat(Math.max(0, count)));
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int n1 = 5, n2 = 6;
        int[] arr11 = {9, 20, 28, 18, 11}, arr12 = {30, 1, 21, 17, 28};
        int[] arr21 = {46, 33, 33, 22, 31, 50}, arr22 = {27, 56, 19, 14, 14, 10};
        System.out.println(Arrays.toString(solution.solution(n1, arr11, arr12)));
        System.out.println(Arrays.toString(solution.solution(n2, arr21, arr22)));
    }
}
