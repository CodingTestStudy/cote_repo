package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class level1_나누어_떨어지는_숫자_배열 {
    static class Solution {
        public int[] solution(int[] arr, int divisor) {
            List<Integer> arrList = new ArrayList<>();
            for (int i = 0; i < arr.length; i++) {
                if (arr[i] % divisor == 0) {
                    arrList.add(arr[i]);
                }
            }
            if (arrList.size() == 0) {
                return new int[]{-1};
            }
            arrList.sort(null);
            int[] answer = new int[arrList.size()];
            for (int i = 0; i < answer.length; i++) {
                answer[i] = arrList.get(i);
            }
            return answer;

            // More Simple Code
//            int[] answer = Arrays.stream(arr).filter(factor -> factor % divisor == 0).toArray();
//            if (answer.length == 0) {
//                answer = new int[]{-1};
//            }
//            Arrays.sort(answer);
//            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] arr1 = {5, 9, 7, 10}, arr2 = {2, 36, 1, 3}, arr3 = {3, 2, 6};
        int divisor1 = 5, divisor2 = 1, divisor3 = 10;
        System.out.println(Arrays.toString(solution.solution(arr1, divisor1)));
        System.out.println(Arrays.toString(solution.solution(arr2, divisor2)));
        System.out.println(Arrays.toString(solution.solution(arr3, divisor3)));
    }
}
