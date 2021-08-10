package level1;

public class level1_자릿수_더하기 {
    public static class Solution {
        public int solution(int n) {
            int answer = 0;
            int x = 10;
            while (n != 0) {
                answer += n % x;
                n /= x;
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(123));
        System.out.println(solution.solution(987));
    }
}
