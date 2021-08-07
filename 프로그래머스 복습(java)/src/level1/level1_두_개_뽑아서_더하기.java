package level1;

import java.util.Arrays;
import java.util.Iterator;
import java.util.TreeSet;

public class level1_두_개_뽑아서_더하기 {
    static class Solution {
        public int[] solution(int[] numbers) {
            TreeSet<Integer> temp = new TreeSet<>();
            for (int i = 0; i < numbers.length - 1; i++) {
                for (int j = i + 1; j < numbers.length; j++) {
                    temp.add(numbers[i] + numbers[j]);
                }
            }
            Iterator<Integer> iter = temp.iterator();
            int[] answer = new int[temp.size()];
            int i = 0;
            while (iter.hasNext()) {
                answer[i] = iter.next();
                i++;
            }
            System.out.println("answer = " + Arrays.toString(answer));
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] nums1 = {2, 1, 3, 4, 1}, nums2 = {5, 0, 2, 7};
        solution.solution(nums1);
        solution.solution(nums2);
    }
}
