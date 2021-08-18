package level2;

public class level2_JadenCase_문자열_만들기 {
    static class Solution {
        public String solution(String s) {
            StringBuilder sb = new StringBuilder();

            if (s.length() == 1) {
                return s.toUpperCase();
            }

            String word = "";
            for (int i = 0; i < s.length(); i++) {
                String substring = s.substring(i, i + 1);
                if (substring.equals(" ")) {
                    sb.append(word);
                    sb.append(" ");

                    word = "";
                } else {
                    if (word.equals("")) {
                        word = substring.toUpperCase();
                    } else {
                        word += substring.toLowerCase();
                    }
                }
            }
            sb.append(word);
            return sb.toString();

            /*
            More Simple Code
            String answer = "";
            String[] sp = s.toLowerCase().split("");
            boolean flag = true;

            for(String ss : sp) {
                answer += flag ? ss.toUpperCase() : ss;
                flag = ss.equals(" ") ? true : false;
            }

            return answer;
             */
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "3people unFollowed me";
        String s2 = "for the last week";
        System.out.println(solution.solution(s1));
        System.out.println(solution.solution(s2));
    }
}
