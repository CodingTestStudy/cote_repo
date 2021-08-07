package level1;

public class level1_짝수와_홀수 {
    static class Solution {
        public String solution(int num) {
            return num % 2 == 0 ? "Even" : "Odd";
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(3));
        System.out.println(solution.solution(4));
    }
}
