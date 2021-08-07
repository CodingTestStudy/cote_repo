package level1;

public class level1_정수_제곱근_판별 {
    static class Solution {
        public long solution(long n) {
            if (Math.sqrt(n)==(int)Math.sqrt(n)) {
                return (long) Math.pow(Math.sqrt(n) + 1, 2);
            } else {
                return -1;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(121));
        System.out.println(solution.solution(3));
    }
}
