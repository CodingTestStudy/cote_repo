package level1;

public class level1_신규_아이디_추천 {
    static class Solution {
        public String solution(String new_id) {
            StringBuilder sb = new StringBuilder(new_id);
            step1(sb);
            step2(sb);
            step3(sb);
            step4(sb);
            step5(sb);
            step6(sb);
            step7(sb);
            return sb.toString();
        }

        private void step7(StringBuilder sb) {
            if (sb.length() <= 2) {
                while (sb.length() != 3) {
                    sb.append(sb.charAt(sb.length() - 1));
                }
            }
        }

        private void step6(StringBuilder sb) {
            if (sb.length() >= 16) {
                sb.delete(15, sb.length());
                step4(sb);
            }
        }

        private void step5(StringBuilder sb) {
            if (sb.length() == 0) {
                sb.append("a");
            }
        }

        private void step4(StringBuilder sb) {
            if (sb.length() > 0 && sb.charAt(0) == '.') {
                sb.deleteCharAt(0);
            }
            if (sb.length() > 0 && sb.charAt(sb.length() - 1) == '.') {
                sb.deleteCharAt(sb.length() - 1);
            }
        }

        private void step3(StringBuilder sb) {
            for (int i = 0; i < sb.length() - 1; i++) {
                if (sb.charAt(i) == '.' && sb.charAt(i + 1) == '.') {
                    sb.deleteCharAt(i);
                    i--;
                }
            }
        }

        private void step2(StringBuilder sb) {
            for (int i = 0; i < sb.length(); i++) {
                char c = sb.charAt(i);
                if (Character.isDigit(c) || Character.isAlphabetic(c)
                        || c == '-' || c == '_' || c == '.') {

                } else {
                    sb.deleteCharAt(i);
                    i--;
                }
            }
        }

        private void step1(StringBuilder sb) {
            //SIMPLE CODE
            //String s = sb.toString().toLowerCase();
            //s 소문자 처리 후, StringBuilder
            for (int i = 0; i < sb.length(); i++) {
                char c = sb.charAt(i);
                if (Character.isAlphabetic(c)) {
                    if (Character.isUpperCase(c)) {
                        sb.setCharAt(i, Character.toLowerCase(c));
                    }
                }
            }
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("...!@BaT#*..y.abcdefghijklm"));
        System.out.println(solution.solution("z-+.^."));
        System.out.println(solution.solution("=.="));
        System.out.println(solution.solution("123_.def"));
        System.out.println(solution.solution("abcdefghijklmn.p"));
    }
}
