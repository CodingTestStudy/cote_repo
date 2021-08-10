package level1;

public class level1_문자열을_정수로_바꾸기 {
    static class Solution {
        public int solution(String s) {
            return Integer.parseInt(s);
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("1234"));
        System.out.println(solution.solution("-1234"));
    }
}
