package level2;

import jdk.swing.interop.SwingInterOpUtils;

import java.lang.management.MemoryType;

public class level2_땅따먹기 {
    static class Solution {
        int solution(int[][] land) {
            int answer = 0;
            for (int i = 0; i < land.length - 1; i++) {
                land[i + 1][0] += Math.max(land[i][1], Math.max(land[i][2], land[i][3]));
                land[i + 1][1] += Math.max(land[i][0], Math.max(land[i][2], land[i][3]));
                land[i + 1][2] += Math.max(land[i][0], Math.max(land[i][1], land[i][3]));
                land[i + 1][3] += Math.max(land[i][0], Math.max(land[i][1], land[i][2]));
            }
            int len = land.length - 1;
            answer = Math.max(Math.max(land[len][0], land[len][1]), Math.max(land[len][2], land[len][3]));
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[][] land = {{1, 2, 3, 5}, {5, 6, 7, 8}, {4, 3, 2, 1}};
        System.out.println(solution.solution(land));
    }
}
