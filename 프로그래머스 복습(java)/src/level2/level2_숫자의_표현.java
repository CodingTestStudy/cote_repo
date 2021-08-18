package level2;

public class level2_숫자의_표현 {
    static class Solution {
        public int solution(int n) {
            int answer = 1;
            for (int i = 1; i < (int) (n / 2) + 1; i++) {
                int x = 0;
                for (int j = i; j < n; j++) {
                    x += j;
                    if (x == n) {
                        answer++;
                        break;
                    } else if (x > n) {
                        break;
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(15));
    }
}
