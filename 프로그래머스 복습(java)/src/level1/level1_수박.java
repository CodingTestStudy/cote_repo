package level1;

public class level1_수박 {
    static class Solution {
        public String solution(int n) {
            StringBuilder sb = new StringBuilder();
            for (int i = 0; i < n; i++) {
                if (i % 2 == 0) {
                    sb.append("수");
                } else {
                    sb.append("박");
                }
            }
            return sb.toString();
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(3));
        System.out.println(solution.solution(4));
    }
}
