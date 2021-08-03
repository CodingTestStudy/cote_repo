public class level1_내적 {
    static class Solution {
        public int solution(int[] a, int[] b) {
            int answer = 0;
            for (int i = 0; i < a.length; i++) {
                answer += a[i] * b[i];
            }
            System.out.println("answer = " + answer);
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int a[] = {1, 2, 3, 4};
        int b[] = {-3, -1, 0, 2};
        int c[] = {-1, 0, 1};
        int d[] = {1, 0, -1};
        System.out.println(solution.solution(a, b));
        System.out.println(solution.solution(c, d));
    }
}
