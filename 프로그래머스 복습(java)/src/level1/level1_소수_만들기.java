package level1;

public class level1_소수_만들기 {
    static class Solution {

        public boolean isPrime(int num) {
            for (int i = 2; i < Math.sqrt(num) + 1; i++) {
                if (num % i == 0) {
                    return false;
                }
            }
            return true;
        }
        public int solution(int[] nums) {
            int answer = 0;
            for (int i = 0; i < nums.length - 2; i++) {
                for (int j = i + 1; j < nums.length - 1; j++) {
                    for (int k = j + 1; k < nums.length; k++) {
                        int sum_value = nums[i] + nums[j] + nums[k];
                        if (isPrime(sum_value)) {
                            answer++;
                        }
                    }
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {1, 2, 3, 4}, nums2 = {1, 2, 7, 6, 4};
        solution.solution(nums1);
        solution.solution(nums2);
    }
}
