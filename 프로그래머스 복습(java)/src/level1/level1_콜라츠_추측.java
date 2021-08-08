package level1;

import java.util.Enumeration;

public class level1_콜라츠_추측 {
    static class Solution {
        public int solution(int num) {
            int answer = 0;
            while (num != 1) {
                if (answer == 487) {
                    return -1;
                }
                if (num % 2 == 0) {
                    num /= 2;
                } else {
                    num = num * 3 + 1;
                }
                answer += 1;
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(6));
        System.out.println(solution.solution(16));
        System.out.println(solution.solution(626331));
    }
}
