package level1;

public class level1_두_정수_사이의_합 {
    static class Solution {
        public long solution(int a, int b) {
            if (a > b) {
                int temp = a;
                a = b;
                b = temp;
            }

            return (long) (b + a) * (b - a + 1) / 2;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(3, 5));
        System.out.println(solution.solution(3, 3));
        System.out.println(solution.solution(5, 3));
    }
}
