package level1;

import java.util.Arrays;
import java.util.Collections;

public class level1_정수_내림차순으로_배치하기 {
    static class Solution {
        public long solution(long n) {
            long answer = 0;
            String[] array = String.valueOf(n).split("");
            Arrays.sort(array);
            Collections.reverse(Arrays.asList(array));
            answer = Long.parseLong(String.join("", array));
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        System.out.println(solution.solution(118372));
    }
}
