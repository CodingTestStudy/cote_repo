import java.util.HashSet;

public class level1_포켓몬 {
    static class Solution {
        public int solution(int[] nums) {
            int canGet = nums.length / 2;
            HashSet<Integer> answer = new HashSet<Integer>();
            for (int i = 0; i < nums.length; i++) {
                answer.add(nums[i]);
            }
            return Math.min(canGet, answer.size());
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {3, 1, 2, 3}, nums2 = {3, 3, 3, 2, 2, 4}, nums3 = {3, 3, 3, 2, 2, 2};
        System.out.println(solution.solution(nums1));
        System.out.println(solution.solution(nums2));
        System.out.println(solution.solution(nums3));
    }
}
