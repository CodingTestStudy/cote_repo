package level1;

public class level1_핸드폰_번호_가리기 {
    static class Solution {
        public String solution(String phone_number) {
            String answer = "";
            for (int i = 0; i < phone_number.length() - 4; i++) {
                answer += "*";
            }
            String substring = phone_number.substring(phone_number.length() - 4);
            return answer + substring;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution("01033334444"));
        System.out.println(solution.solution("027778888"));

    }
}
