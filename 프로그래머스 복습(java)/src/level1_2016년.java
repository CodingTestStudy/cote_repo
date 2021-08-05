public class level1_2016년 {
    static class Solution {
        public String solution(int a, int b) {
            String[] answer = {"THU", "FRI", "SAT", "SUN", "MON", "TUE", "WED"};
            int[] month = {0, 31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31};
            int days = 0;
            for (int i = 1; i < a; i++) {
                days += month[i];
            }
            days += b;
            return answer[days % 7];
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int a = 5, b = 24;
        System.out.println(solution.solution(a, b));
    }
}
