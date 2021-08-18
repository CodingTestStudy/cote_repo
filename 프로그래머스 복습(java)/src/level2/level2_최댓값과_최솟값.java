package level2;

import java.util.ArrayList;
import java.util.List;

public class level2_최댓값과_최솟값 {
    static class Solution {
        public String solution(String s) {
            String answer = "";
            String[] sp = s.split(" ");
            List<Integer> list = new ArrayList<>();
            for (String s1 : sp) {
                list.add(Integer.parseInt(s1));
            }
            list.sort(null);
            answer = String.valueOf(list.get(0)) + " " + String.valueOf(list.get(list.size() - 1));
            return answer;
        }
    }

    public static void main(String[] args) {
        Solution solution = new Solution();
        String s1 = "1 2 3 4";
        String s2 = "-1 -2 -3 -4";
        String s3 = "-1 -1";
        System.out.println(solution.solution(s1));
        System.out.println(solution.solution(s2));
        System.out.println(solution.solution(s3));
    }
}
