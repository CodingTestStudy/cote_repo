package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class level1_같은_숫자는_싫어 {
    public static class Solution {
        public int[] solution(int []arr) {
            if (arr.length == 0) {
                return new int[]{};
            }
            List<Integer> answerList = new ArrayList<>();
            answerList.add(arr[0]);
            for (int i = 1; i < arr.length; i++) {
                if (arr[i] != arr[i - 1]) {
                    answerList.add(arr[i]);
                }
            }
            int[] answer = new int[answerList.size()];
            for (int i = 0; i < answer.length; i++) {
                answer[i] = answerList.get(i);
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {1, 1, 3, 3, 0, 1, 1}, arr2 = {4, 4, 4, 3, 3};
        System.out.println(Arrays.toString(solution.solution(arr1)));
        System.out.println(Arrays.toString(solution.solution(arr2)));
    }
}
