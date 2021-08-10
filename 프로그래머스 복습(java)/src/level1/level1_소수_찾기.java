package level1;

public class level1_소수_찾기 {
    static class Solution {
        public Boolean isPrime(int n) {
            for (int i = 2; i < Math.sqrt(n) + 1; i++) {
                if (n % i == 0) {
                    return false;
                }
            }
            return true;
        }

        public int solution(int n) {
            int answer = 0;
            for (int i = 1; i < n + 1; i++) {
                if (isPrime(i)) {
                    answer++;
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(10));
        System.out.println(solution.solution(5));
    }
}
