package level2;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Collections;
import java.util.List;

public class level2_최솟값_만들기 {
    static class Solution {
        public int solution(int[] A, int[] B) {
            int answer = 0;
            Arrays.sort(A);
            List<Integer> list = new ArrayList<>();
            for (int i : B) {
                Integer integer = i;
                list.add(integer);
            }
            Integer[] C = list.toArray(new Integer[0]);
            Arrays.sort(C, Collections.reverseOrder());
            for (int i = 0; i < A.length; i++) {
                answer += A[i] * C[i];
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        int[] A1 = {1, 4, 2}, B1 = {5, 4, 4};
        int[] A2 = {1, 2}, B2 = {3, 4};
        System.out.println(solution.solution(A1, B1));
        System.out.println(solution.solution(A2, B2));
    }
}
