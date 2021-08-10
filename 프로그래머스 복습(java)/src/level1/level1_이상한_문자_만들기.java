package level1;

import java.util.Locale;

public class level1_이상한_문자_만들기 {
    static class Solution {
        public String solution(String s) {
            String answer = "";
            String[] sp = s.split("");
            int x = 0;
            for (int i = 0; i < sp.length; i++) {
                if (sp[i].equals(" ")) {
                    x = 0;
                    answer += " ";
                } else {
                    if (x % 2 == 0) {
                        answer += sp[i].toUpperCase();
                    } else {
                        answer += sp[i].toLowerCase();
                    }
                    x += 1;
                }
            }
            return answer;

            //More Simple Code
//            String answer = "";
//            int cnt = 0;
//            String[] array = s.split(" ");
//            for (String ss : array) {
//                cnt = ss.contains(" ") ? 0 : cnt + 1;
//                answer += cnt % 2 == 0 ? ss.toLowerCase() : ss.toUpperCase();
//            }
//            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("try hello world"));
    }
}
