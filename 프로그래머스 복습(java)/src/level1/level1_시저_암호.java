package level1;

public class level1_시저_암호 {
    static class Solution {
        public String solution(String s, int n) {
            String answer = "";
            char[] c = s.toCharArray();
            for (int i = 0; i < s.length(); i++) {
                char alpha = c[i];
                if (alpha == ' ') {
                    answer += ' ';
                } else if (alpha >= 'a' && alpha <= 'z') {
                    if (alpha + n > 'z') {
                        answer += (char) (alpha + n - 26);
                    } else {
                        answer += (char) (alpha + n);
                    }
                } else {
                    if (alpha + n > 'Z') {
                        answer += (char) (alpha + n - 26);
                    } else {
                        answer += (char) (alpha + n);
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("AB", 1));
        System.out.println(solution.solution("z", 1));
        System.out.println(solution.solution("a B z", 4));
    }
}
