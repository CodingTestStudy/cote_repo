package level1;

public class level1_가운데_글자_가져오기 {
    static class Solution {
        public String solution(String s) {
            int sSize = s.length();
            if (sSize % 2 == 0) {
                return s.substring(sSize / 2 - 1, sSize / 2 + 1);
            } else {
                return s.substring(sSize / 2, sSize/2 + 1);
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "abcde", s2 = "qwer";
        System.out.println(solution.solution(s1));
        System.out.println(solution.solution(s2));
    }
}
