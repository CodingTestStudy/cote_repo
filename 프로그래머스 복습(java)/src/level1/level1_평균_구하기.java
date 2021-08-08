package level1;

public class level1_평균_구하기 {
    static class Solution {
        public double solution(int[] arr) {
            double answer = 0;
            for (int i = 0; i < arr.length; i++) {
                answer += arr[i];
            }
            return answer / arr.length;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {1, 2, 3, 4}, arr2 = {5, 5};
        System.out.println(solution.solution(arr1));
        System.out.println(solution.solution(arr2));
    }
}
