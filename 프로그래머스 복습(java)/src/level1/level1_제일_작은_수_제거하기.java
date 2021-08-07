package level1;

import java.util.ArrayList;
import java.util.Arrays;

public class level1_제일_작은_수_제거하기 {
    static class Solution {
        public int[] solution(int[] arr) {
            if (arr.length == 1) {
                return new int[]{-1};
            }

            int minValue = arr[0];
            int index = 0;
            for (int i = 1; i < arr.length; i++) {
                if (minValue > arr[i]) {
                    minValue = arr[i];
                    index = i;
                }
            }
            int[] answer = new int[arr.length - 1];
            int idx = 0;
            for (int i = 0; i < arr.length; i++) {
                if (i == index) {
                    continue;
                } else {
                    answer[idx] = arr[i];
                    idx++;
                }
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {4, 3, 2, 1}, arr2 = {10};
        System.out.println(Arrays.toString(solution.solution(arr1)));
        System.out.println(Arrays.toString(solution.solution(arr2)));
    }
}
