package level1;

import java.util.HashSet;

public class level1_약수의_합 {
    static class Solution {
        public int solution(int n) {
            int answer = 0;
            HashSet<Integer> hashSet = new HashSet<>();
            for (int i = 1; i < Math.sqrt(n) + 1; i++) {
                if (n % i == 0) {
                    hashSet.add(i);
                    hashSet.add(n / i);
                }
            }
            for (Integer i : hashSet) {
                answer += i;
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(12));
        System.out.println(solution.solution(5));
    }
}
