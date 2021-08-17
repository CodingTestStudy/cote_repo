package level2;

public class level2_N개의_최소공배수 {
    static class Solution {
        int gcd(int x, int y) {
            int temp, n;
            if (x < y) {
                temp = x;
                x = y;
                y = temp;
            }
            while (y != 0) {
                n = x % y;
                x = y;
                y = n;
            }
            return x;
        }

        public int solution(int[] arr) {
            int answer = arr[0];
            for (int i : arr) {
                answer = answer * i / gcd(answer, i);
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {2, 6, 8, 14};
        int[] arr2 = {1, 2, 3};
        System.out.println(solution.solution(arr1));
        System.out.println(solution.solution(arr2));
    }
}
