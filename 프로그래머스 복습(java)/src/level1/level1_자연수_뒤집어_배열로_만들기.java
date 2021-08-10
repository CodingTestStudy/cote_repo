package level1;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;

public class level1_자연수_뒤집어_배열로_만들기 {
    static class Solution {
        public int[] solution(long n) {
            List<Integer> list = new ArrayList<>();
            while (n != 0) {
                list.add((int) (n % 10));
                n /= 10;
            }
            int[] answer = new int[list.size()];
            for (int i = 0; i < list.size(); i++) {
                answer[i] = list.get(i);
            }
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(Arrays.toString(solution.solution(12345)));
    }
}
