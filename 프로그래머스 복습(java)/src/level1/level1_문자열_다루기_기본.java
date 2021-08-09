package level1;

public class level1_문자열_다루기_기본 {
    static class Solution {
        public boolean solution(String s) {
            if (s.length() == 4 || s.length() == 6) {
                char[] c = s.toCharArray();
                for (char c1 : c) {
                    int num = c1 - '0';
                    if (num > 9 || num < 0) {
                        return false;
                    }
                }
                return true;
            } else {
                return false;
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("a234"));
        System.out.println(solution.solution("1234"));
    }
}
