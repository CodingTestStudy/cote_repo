package level1;

import java.util.Arrays;

public class level1_최대공약수와_최소공배수 {
    static class Solution {
        public int gcd(int n, int m) {
            if (n < m) {
                int temp = n;
                n = m;
                m = temp;
            }
            int r = n % m;
            while (r != 0) {
                n = m;
                m = r;
                r = n % m;
            }
            return m;
        }

        public int lcm(int n, int m, int g) {
            return n * m / g;
        }

        public int[] solution(int n, int m) {
            int g = gcd(n, m);
            return new int[]{g, lcm(n, m, g)};
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(3, 12)));
        System.out.println(Arrays.toString(solution.solution(2, 5)));
    }
}
